const redis = require("redis");
const util = require("util");
const kue = require("kue");
const express = require("express");

let reservationEnabled;

const client = redis.createClient();
// By default redis.createClient() will use 127.0.0.1 and port 6379

// listen for the connect event to see whether we successfully connected to the redis-server
client.on("connect", () => {
  console.log("Redis client connected to the server");
  reserveSeat(50);
  reservationEnabled = true;
});

// listen for the error event tocheck if we failed to connect to the redis-server
client.on("error", (err) =>
  console.error(`Redis client not connected to the server: ${err.message}`)
);

const reserveSeat = (number) => {
  client.set("available_seats", number, redis.print);
};

const promiseBasedGet = util.promisify(client.get).bind(client);
const getCurrentAvailableSeats = async () => {
  return await promiseBasedGet("available_seats");
};

const queue = kue.createQueue();

const app = express();

app.get("/available_seats", async (_, res) => {
  res.json({ numberOfAvailableSeats: await getCurrentAvailableSeats() });
});

app.get("/reserve_seat", (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: "Reservation are blocked" });
    return;
  }

  const job = queue.create("reserve_seat").save((err) => {
    if (!err) {
      res.json({ status: "Reservation in process" });
    } else {
      res.json({ status: "Reservation failed" });
    }
  });

  job.on("complete", () =>
    console.log(`Seat reservation job ${job.id} completed`)
  );
  job.on("failed", (err) =>
    console.log(`Seat reservation job ${job.id} failed: ${err}`)
  );
});

app.get("/process", (_, res) => {
  queue.process("reserve_seat", async (_, done) => {
    const availableSeats = Number(await getCurrentAvailableSeats());

    if (availableSeats <= 0) {
      done(Error("Not enough seats available"));
    }

    reserveSeat(availableSeats - 1);

    if (availableSeats === 1) {
      reservationEnabled = false;
    }

    done();
  });
  res.json({ status: "Queue processing" });
});

app.listen(1245, () => {
  console.log("app is listening on port", 1245);
});

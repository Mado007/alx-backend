const redis = require("redis");

// this creates a new client
const publisher = redis.createClient();
// By default redis.createClient() will use 127.0.0.1 and port 6379

// listen for the connect event to see whether we successfully connected to the redis-server
publisher.on("connect", () =>
  console.log("Redis client connected to the server")
);

// listen for the error event tocheck if we failed to connect to the redis-server
publisher.on("error", (err) =>
  console.error(`Redis client not connected to the server: ${err.message}`)
);

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish("holberton school channel", message);
  }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

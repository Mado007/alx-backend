const redis = require("redis");

// this creates a new client
const subscriber = redis.createClient();
// By default redis.createClient() will use 127.0.0.1 and port 6379

// listen for the connect event to see whether we successfully connected to the redis-server
subscriber.on("connect", () => console.log("Redis client connected to the server"));

// listen for the error event tocheck if we failed to connect to the redis-server
subscriber.on("error", (err) =>
  console.error(`Redis client not connected to the server: ${err.message}`)
);

subscriber.subscribe("holberton school channel");

subscriber.on("message", (channel, message) => {
  if (channel === "holberton school channel") {
    console.log(message);
  }

  if (message === "KILL_SERVER") {
    subscriber.unsubscribe("holberton school channel");
    subscriber.quit();
  }
})

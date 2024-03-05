const redis = require("redis");
const util = require("util");

// this creates a new client
const client = redis.createClient();
// By default redis.createClient() will use 127.0.0.1 and port 6379

// listen for the connect event to see whether we successfully connected to the redis-server
client.on("connect", () => console.log("Redis client connected to the server"));

// listen for the error event tocheck if we failed to connect to the redis-server
client.on("error", (err) =>
  console.error(`Redis client not connected to the server: ${err.message}`)
);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const promiseBasedGet = util.promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  console.log(await promiseBasedGet(schoolName));
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

const redis = require("redis");
const util = require("util");

const listProducts = [
  {
    itemId: 1,
    itemName: "Suitcase 250",
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: "Suitcase 450",
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: "Suitcase 650",
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: "Suitcase 1050",
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const getItemById = (id) => {
  return listProducts.find((element) => element.itemId === id);
};

const express = require("express");

const app = express();

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

app.listen(1245, () => {
  console.log("app is listening on port", 1245);
});

const client = redis.createClient();
// By default redis.createClient() will use 127.0.0.1 and port 6379

client.on("connect", () => console.log("Redis client connected to the server"));

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, redis.print);
};

const promiseBasedGet = util.promisify(client.get).bind(client);
const getCurrentReservedStockById = async (itemId) => {
  const stock = await promiseBasedGet(`item.${itemId}`);
  return stock;
};

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: "Product not found" });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);

  if (!currentStock) {
    await reserveStockById(itemId, item.initialAvailableQuantity);
    item.currentQuantity = item.initialAvailableQuantity;
  } else {
    item.currentQuantity = currentStock;
  }

  res.json(item);
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: "Product not found" });
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) {
    currentStock = item.initialAvailableQuantity;
  }

  if (currentStock <= 0) {
    res.json({ status: "Not enough stock available", itemId: 1 });
    return;
  }

  reserveStockById(itemId, Number(currentStock) - 1);

  res.json({ status: "Reservation confirmed", itemId: 1 });
});

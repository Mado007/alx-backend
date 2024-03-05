# Simple Queue System in JavaScript

Welcome to the Simple Queue System repository! This project, part of the Web Stack Programming specialization at Holberton School, introduces you to the basics of queuing systems in JavaScript.

## Objectives

In this project, you will:

- Set up and run a local Redis server.
- Perform fundamental operations using the Redis client.
- Explore asynchronous operations with Redis.
- Implement Kue for queue management.
- Build basic Express applications that interact with Redis and queues.

## Dependencies

Ensure you have the following dependencies installed:

### `package.json`

```json
{
    "name": "simple-queue-system-js",
    "version": "1.0.0",
    "description": "A simple queue system in JavaScript",
    "main": "index.js",
    "scripts": {
        "lint": "./node_modules/.bin/eslint",
        "check-lint": "lint [0-9]*.js",
        "test": "./node_modules/.bin/mocha --require @babel/register --exit",
        "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "license": "ISC",
    "dependencies": {
        "chai-http": "^4.3.0",
        "express": "^4.17.1",
        "kue": "^0.11.6",
        "redis": "^2.8.0"
    },
    "devDependencies": {
        "@babel/cli": "^7.8.0",
        "@babel/core": "^7.8.0",
        "@babel/node": "^7.8.0",
        "@babel/preset-env": "^7.8.2",
        "@babel/register": "^7.8.0",
        "eslint": "^6.4.0",
        "eslint-config-airbnb-base": "^14.0.0",
        "eslint-plugin-import": "^2.18.2",
        "eslint-plugin-jest": "^22.17.0",
        "nodemon": "^2.0.2",
        "chai": "^4.2.0",
        "mocha": "^6.2.2",
        "request": "^2.88.0",
        "sinon": "^7.5.0"
    }
}
```

### `.babelrc`

```json
{
    "presets": [
        "@babel/preset-env"
    ]
}
```
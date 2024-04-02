// serverless-function.js
const { createServer } = require('@vercel/node');
const { app } = require('./myflask');

module.exports = createServer(app);

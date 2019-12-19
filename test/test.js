const hashing = require("..");
const crypto = require("crypto")

let data = new Buffer.from(crypto.randomBytes(100), "hex");

let hashedData = hashing.hash(data);
console.log(hashedData.toString('hex'))

#!/usr/bin/node
const args = require('process').argv;

for (let i = 2; i < args.length; i++) {
  console.log(args[i]);
}

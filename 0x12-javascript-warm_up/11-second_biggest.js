#!/usr/bin/node

const args = require('process').argv;

if (args.length < 4) console.log(0);

else {
  const sorted = (args.slice(2)).sort(function (a, b) { return b - a; });
  console.log(sorted[1]);
}

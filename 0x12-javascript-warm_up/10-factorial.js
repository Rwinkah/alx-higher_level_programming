#!/usr/bin/node
const args = require('process').argv;

function fact (num) {
  if (Number.isNaN(Number(num))) return (1);
  if (Number(num) === 1) return (1);
  return (num * fact(num - 1));
}
console.log(fact(args[2]));

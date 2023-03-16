#!/usr/bin/node
const args = require('process').argv;
const myVar = Number(args[2]);

if (Number.isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log(myVar);
}

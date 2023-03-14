#!/usr/bin/node
const args = require('process').argv;
const myVar = Number(args[2]);

if (Number.isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node
const args = require('process').argv;
const myVar = Number(args[2]);
let outpt = '';
if (Number.isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    for (let j = 0; j < myVar; j++) {
      outpt += 'X';
    }
    console.log(outpt);
    outpt = '';
  }
}

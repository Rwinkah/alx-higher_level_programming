#!/usr/bin/node
const myVar = (require('process').argv).length;
if (myVar === 2) {
  console.log('No argument');
} else if (myVar === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

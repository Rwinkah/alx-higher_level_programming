#!/usr/bin/node
const args = (require('process')).argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}

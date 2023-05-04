#!/usr/bin/node
const converter = require('./10-converter').converter;

let myconv = converter(10);

console.log(myconv(2));
console.log(myconv(12));
console.log(myconv(89));

myconv = converter(16);

console.log(myconv(2));
console.log(myconv(12));
console.log(myconv(89));

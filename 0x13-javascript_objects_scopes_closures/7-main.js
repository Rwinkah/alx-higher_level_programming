#!/usr/bin/node
const nbo = require('./7-occurrences').nbOccurrences;

console.log(nbo([1, 2, 3, 4, 5, 6], 3));
console.log(nbo([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbo(['S', 12, 'c', 'S', 'School', 8], 'S'));

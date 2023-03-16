#!/usr/bin/node

const { dict } = require('./101-data.js');
const nDict = {};
for (const [id, occ] of Object.entries(dict)) {
  if (!nDict[occ]) {
    nDict[occ] = [];
  }
  nDict[occ].push(id);
}
console.log(nDict);

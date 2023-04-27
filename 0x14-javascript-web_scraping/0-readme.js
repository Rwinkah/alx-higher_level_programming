#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.readFile(process.argv[2], 'utf8', function (err, fileContent) {
  console.log(err || fileContent);
});

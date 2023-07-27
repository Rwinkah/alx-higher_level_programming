#!/usr/bin/node
/* Writting to a file using nodejs */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});

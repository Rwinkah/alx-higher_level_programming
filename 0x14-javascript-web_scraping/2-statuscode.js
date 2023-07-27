#!/usr/bin/node
/* Display Status code of get request */
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});

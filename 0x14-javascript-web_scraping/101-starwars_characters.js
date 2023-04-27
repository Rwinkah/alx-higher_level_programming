#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(apiUrl, function (error, response, body) {
  if (!error) {
    const charUrls = JSON.parse(body).characters;
    printCharacters(charUrls, 0);
  }
});

function printCharacters (charUrls, index) {
  request(charUrls[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < charUrls.length) {
        printCharacters(charUrls, index + 1);
      }
    }
  });
}

#!/usr/bin/node

const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const respInfo = JSON.parse(body);
    console.log(respInfo.title);
  }
});

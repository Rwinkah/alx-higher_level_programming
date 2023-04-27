#!/usr/bin/node

const request = require('request');
const response = request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  console.log(response.statusCode)
  if (error) {
    console.log(error)
  }
  else if (response.statusCode == 200) {
    const respInfo = JSON.parse(body)
    console.log(respInfo.title)
  }
})

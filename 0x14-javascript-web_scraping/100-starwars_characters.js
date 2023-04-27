#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

// Make a GET request to the SWAPI Films API with the specified film ID
request.get(apiUrl + filmId, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  // Parse the response body as JSON
  const filmData = JSON.parse(body);

  // Extract the characters array from the film data
  const characters = filmData.characters;

  // Iterate over each character URL in the array and make a GET request to it
  for (const characterUrl of characters) {
    request.get(characterUrl, function (err, res, body) {
      if (err) {
        console.log(err);
        return;
      }
      // Parse the character data as JSON and log the character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});


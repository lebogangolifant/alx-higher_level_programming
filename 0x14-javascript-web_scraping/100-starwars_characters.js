#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) {
    console.log('code:', response && response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    jsonBody.characters.forEach(character => {
      request(character, (errorC, responseC, bodyC) => {
        if (errorC) {
          console.log('code:', responseC && responseC.statusCode);
        }
        console.log(JSON.parse(bodyC).name);
      });
    });
  }
});

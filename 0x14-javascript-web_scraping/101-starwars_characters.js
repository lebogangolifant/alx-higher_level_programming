#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie in order
 */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function printCharactersInOrder (characters, index) {
  if (index === characters.length) {
    return;
  }
  request(characters[index], function (errorC, responseC, bodyC) {
    if (errorC) {
      console.log('code:', responseC && responseC.statusCode);
    } else {
      const characterData = JSON.parse(bodyC);
      console.log(characterData.name);
      printCharactersInOrder(characters, index + 1);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response && response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    printCharactersInOrder(jsonBody.characters, 0);
  }
});

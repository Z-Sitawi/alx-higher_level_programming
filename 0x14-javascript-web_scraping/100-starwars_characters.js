#!/usr/bin/node
/* prints all characters of a Star Wars movie
based on a given Movie id
Usage: ./100-starwars_charachter.js <movieId (int)> */

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const request = require('request');
  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
  request(url, function (error, response) {
    if (error) {
      console.log(error);
    } else {
      const characters = JSON.parse(response.body).characters;
      for (const character of characters) {
        const cUrl = character + '?format=json';
        request(cUrl, function (error, res, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}

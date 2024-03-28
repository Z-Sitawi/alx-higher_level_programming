#!/usr/bin/node
/* prints the title of a Star Wars movie where
the episode number matches a given integer. */
if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
  const request = require('request');
  request(url, function (error = null, response) {
    console.log(JSON.parse(response.body).title);
  });
}

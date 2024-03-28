#!/usr/bin/node
/* prints the number of movies where
the character “Wedge Antilles” is present. */
if (process.argv.length > 2) {
  const url = process.argv[2];
  let count = 0;
  const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
  const request = require('request');
  request(url, function (error, response) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(response.body).results;
      for (const film of films) {
        for (const character of film.characters) {
          if (character === wedge) { count++; }
        }
      }
      console.log(count);
    }
  });
}

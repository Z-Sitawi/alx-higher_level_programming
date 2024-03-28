#!/usr/bin/node
/* prints the number of movies where
the character “Wedge Antilles” is present. */
if (process.argv.length > 2) {
  const url = process.argv[2];
  let count = 0;
  const request = require('request');
  request(url, function (error, response) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(response.body).results;
      for (const film of films) {
        for (const character of film.characters) {
          if (character.includes(18)) { count++; }
        }
      }
      console.log(count);
    }
  });
}

#!/usr/bin/node
/* prints all characters of a Star Wars movie
based on a given Movie id (sorted)
Usage: ./100-starwars_charachter.js <movieId (int)> */

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;

    const getNumberFromUrl = (url) => {
      const parts = url.split('/');
      return parseInt(parts[parts.length - 2]);
    };

    // Sort the characters array based on the number in the URL
    characters.sort((a, b) => {
      const numberA = getNumberFromUrl(a);
      const numberB = getNumberFromUrl(b);
      return numberA - numberB;
    });

    // Function to fetch character details and print them sequentially
    const fetchAndPrintCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
            resolve();
          }
        });
      });
    };

    // Sequentially fetch and print each character
    characters.reduce((promiseChain, characterUrl) => {
      return promiseChain.then(() => fetchAndPrintCharacter(characterUrl));
    }, Promise.resolve());
  }
});

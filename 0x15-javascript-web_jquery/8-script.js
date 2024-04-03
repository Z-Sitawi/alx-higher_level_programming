#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response not ok');
    }
    return response.json();
  })
  .then(data => {
    const allFilms = data.results;
    allFilms.forEach(film => {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  })
  .catch(error => {
    console.log('Error fetching data:', error);
  });

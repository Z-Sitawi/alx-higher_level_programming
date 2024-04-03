#!/usr/bin/node

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response not ok');
    }
    return response.json();
  })
  .then(data => {
    $('#hello').text(data.hello);
  })
  .catch(error => {
    console.log('Error fetching data:', error);
  });

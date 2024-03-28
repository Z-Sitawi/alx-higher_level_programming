#!/usr/bin/node
/* Display the status code of a GET request. */
if (process.argv.length > 2) {
  const url = process.argv[2];
  const request = require('request');
  request(url, function (error = null, response) {
    console.log('code:', response.statusCode);
  });
}

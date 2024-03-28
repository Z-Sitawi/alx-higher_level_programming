#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file. */
if (process.argv.length > 2) {
  const url = process.argv[2];
  const path = process.argv[3];
  const request = require('request');
  const fs = require('fs');
  request(url, function (error, response, body) {
    if (error) { console.log(error); } else {
      fs.writeFile(path, body, 'utf-8', (err) => {
        if (err) { console.log(err); }
      });
    }
  });
}

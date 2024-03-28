#!/usr/bin/node
/* reads and prints the content of a file. */
const argvLength = process.argv.length;
if (argvLength > 2) {
  const fs = require('fs');
  const file = process.argv[2];

  fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

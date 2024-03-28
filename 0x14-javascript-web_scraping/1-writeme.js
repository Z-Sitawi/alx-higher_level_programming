#!/usr/bin/node
/* writes a string to a file. */
const argvLength = process.argv.length;
if (argvLength > 3) {
  const fs = require('fs');
  const file = process.argv[2];
  const content = process.argv[3];

  fs.writeFile(file, content, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

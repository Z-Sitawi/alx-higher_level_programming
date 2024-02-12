#!/usr/bin/node
const argv = process.argv;
const firstArg = parseInt(argv[2]);
if (!isNaN(firstArg)) {
  console.log('My number:', firstArg);
} else {
  console.log('Not a number');
}

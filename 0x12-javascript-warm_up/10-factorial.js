#!/usr/bin/node
const firstArg = process.argv[2];

function factorial (num) {
  num = parseInt(num);
  if (isNaN(num)) {
    return 1;
  } else {
    if (num === 0) {
      return 0;
    }
    num += factorial(num - 1);
  }
  return num;
}

console.log(factorial(firstArg));

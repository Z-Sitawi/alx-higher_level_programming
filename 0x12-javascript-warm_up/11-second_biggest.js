#!/usr/bin/node
const argvArray = process.argv;
let secondBiggest;
const newArray = [];
if (argvArray.length <= 3) {
  secondBiggest = 0;
} else {
  for (let i = 2; i < argvArray.length; i++) {
    newArray[i - 2] = parseInt(argvArray[i]);
  }
  newArray.sort((a, b) => b - a);
  secondBiggest = newArray[1];
}
console.log(secondBiggest);

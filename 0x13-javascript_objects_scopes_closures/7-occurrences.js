#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let count = 0;
  for (let x = 0; x < len; x++) {
    if (list[x] === searchElement) {
      count = count + 1;
    }
  }
  return count;
};

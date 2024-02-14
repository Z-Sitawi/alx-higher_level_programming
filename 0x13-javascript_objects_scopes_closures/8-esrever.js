#!/usr/bin/node
exports.esrever = function (list) {
  // returen a reversed list
  const reversedList = [];
  let idx = 0;
  for (let i = list.length - 1; i > -1; i--) {
    reversedList[idx] = list[i];
    idx++;
  }
  return reversedList;
};

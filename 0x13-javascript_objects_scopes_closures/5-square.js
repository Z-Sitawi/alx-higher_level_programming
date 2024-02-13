#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size, w = 0, h = 0) {
    super(w = size, h = size);
  }
}

module.exports = Square;

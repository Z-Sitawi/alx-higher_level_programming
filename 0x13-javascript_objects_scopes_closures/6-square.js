#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size, w = 0, h = 0) {
    super(w = size, h = size);
  }

  charPrint (c) {
    // prints the square using the character c If defined else uses the character X
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
}

module.exports = Square;

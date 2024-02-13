#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // prints the rectangle.
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    // exchanges the width and the height of the rectangle.
    const tmpWidth = this.width;
    this.width = this.height;
    this.height = tmpWidth;
  }

  double () {
    // multiples the width and the height of the rectangle by 2.
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;

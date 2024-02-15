#!/usr/bin/node
// instantiate rotate() and double()
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // exchange width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // multiply width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

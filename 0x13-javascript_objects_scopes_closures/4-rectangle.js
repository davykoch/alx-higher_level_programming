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

	rotate
  }
  
  module.exports = Rectangle;
  
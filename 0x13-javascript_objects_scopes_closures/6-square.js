#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    const prch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let squa = '';
      for (let j = 0; j < this.width; j++) {
        squa += prch;
      }
      console.log(squa);
    }
  }
}

module.exports = Square;

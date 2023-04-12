#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (ch = 'X') {
    for (let i = 0; i < this.height; i++) console.log(ch.repeat(this.width));
  }
};

#!/usr/bin/node
const PSquare = require('./5-square');
module.exports = class Square extends PSquare {
  charPrint (ch = 'X') {
    for (let i = 0; i < this.height; i++) console.log(ch.repeat(this.width));
  }
};

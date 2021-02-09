#!/usr/bin/node
const Mraba3 = require('./5-square');
class Square extends Mraba3 {
  charPrint (ch) {
    if (ch === undefined) {
      ch = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log((ch).repeat(this.width));
    }
  }
}
module.exports = Square;

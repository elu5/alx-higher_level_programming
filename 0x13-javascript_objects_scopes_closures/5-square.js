#!/usr/bin/node
const Square = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
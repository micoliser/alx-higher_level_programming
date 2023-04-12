#!/usr/bin/node
let timesCalled = 0;
exports.logMe = function (item) {
  console.log(`${timesCalled}: ${item}`);
  timesCalled++;
};

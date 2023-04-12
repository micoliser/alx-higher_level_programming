#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  for (const item of list) reversedList.unshift(item);
  return reversedList;
};

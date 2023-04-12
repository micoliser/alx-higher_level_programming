#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};

Object.keys(dict).map((key, index) => {
  if (newDict[dict[key]] === undefined) newDict[dict[key]] = [];
  newDict[dict[key]].push(key);
  return index;
});

console.log(newDict);

#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);
if (Number.isNaN(num)) console.log('Not a number');
else console.log(`My number: ${num}`);

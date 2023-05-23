#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const fileName = args[0];
const str = args[1];

fs.writeFile(fileName, str, (err, data) => {
  if (err) console.log(err);
});

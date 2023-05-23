#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    film.characters.forEach(character => {
      if (character.includes('18')) count++;
    });
  }
  console.log(count);
});

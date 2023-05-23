#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    if (film.characters.includes(wedgeUrl)) count++;
  }

  console.log(count);
});

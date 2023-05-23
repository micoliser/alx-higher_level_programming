#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const id = args[0];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getEndpoints () {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) reject(err);
      resolve(JSON.parse(body).characters);
    });
  });
}

async function getCharacters (characters) {
  for (const character of characters) await getCharacter(character);
}

function getCharacter (character) {
  return new Promise((resolve, reject) => {
    request.get(character, (err, res, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
      resolve();
    });
  });
}

getEndpoints()
  .then(data => {
    return getCharacters(data);
  })
  .catch(err => {
    console.log(err);
  });

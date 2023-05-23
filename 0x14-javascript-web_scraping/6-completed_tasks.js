#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const obj = {};

request(url, (err, res, body) => {
  if (err) console.log(err);
  const tasks = JSON.parse(body);

  for (const task of tasks) {
    const id = task.userId.toString();
    if (!Object.keys(obj).includes(id) && task.completed) {
      obj[id] = 1;
      continue;
    }
    if (task.completed) obj[id]++;
  }

  console.log(obj);
});

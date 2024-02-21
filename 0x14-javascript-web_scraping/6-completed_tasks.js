#!/usr/bin/node
/* count completed tasks for all users */
const request = require('request');

const x = process.argv;
if (x.length !== 3) {
  console.log('usage: appname + url');
  process.exit(1);
}

const url = x[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    const jsonRes = JSON.parse(body);
    for (const i in jsonRes) {
      const task = jsonRes[i];
      if (task.completed === true) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 1;
        } else {
          dict[task.userId]++;
        }
      }
    }
    console.log(dict);
  }
});

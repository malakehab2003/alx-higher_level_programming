#!/usr/bin/node
/* get the name of the movie of passed id */
const request = require('request');

const x = process.argv;
if (x.length !== 3) {
  console.log('usage: appname + id');
  process.exit(1);
}

const id = x[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonRes = JSON.parse(body);
    console.log(jsonRes.title);
  }
});

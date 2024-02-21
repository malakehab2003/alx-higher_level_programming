#!/usr/bin/node
/* get names of all chars in a movie */
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
    for (const i in jsonRes.characters) {
      const chars = jsonRes.characters;
      request(chars[i], (error, response, data) => {
        if (error) {
          console.log(error);
        } else {
          const people = JSON.parse(data);
          console.log(people.name);
        }
      });
    }
  }
});

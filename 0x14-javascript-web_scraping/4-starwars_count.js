#!/usr/bin/node
/* get number of movies of Wedge Antilles */
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
  } else if (res.statusCode === 200) {
    let count = 0;
    const jsonRes = JSON.parse(body).results;
    for (const index in jsonRes) {
      const chars = jsonRes[index].characters;
      for (const i in chars) {
        if (chars[i].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});

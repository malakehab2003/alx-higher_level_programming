#!/usr/bin/node
/* get contents of a webpage and stores it in a file */
const request = require('request');
const fs = require('fs');

const x = process.argv;
if (x.length !== 4) {
  console.log('usage: appname + url + filepath');
  process.exit(1);
}

const url = x[2];
const file = x[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (err) {
        console.log(error);
      }
    });
  }
});

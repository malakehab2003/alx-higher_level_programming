#!/usr/bin/node
/* send a GET request and print the status code */
const request = require('request');

const x = process.argv;
if (x.length !== 3) {
  console.log('usage: appname + url');
  process.exit(1);
}

const url = x[2];

request(url, (err, res) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', res.statusCode);
});

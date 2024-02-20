#!/usr/bin/node
/* read and print the content of a file */
const fs = require('fs');

const x = process.argv;
if (x.length !== 3) {
  console.log('usage: appname + filename');
  process.exit(1);
}

const file = x[2];

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

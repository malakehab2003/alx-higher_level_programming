#!/usr/bin/node
/* write a string in a file */

const fs = require('fs');

const x = process.argv;
if (x.length !== 4) {
  console.log('usage: appname + filepath + text');
  process.exit(1);
}

const file = x[2];

fs.writeFile(file, x[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

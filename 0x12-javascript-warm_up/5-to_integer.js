#!/usr/bin/node

const arg1 = process.argv[2];

const converted = parseInt(arg1);

if (isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + converted);
}

#!/usr/bin/node

const x = process.argv[2];

const converted = parseInt(x);

if (isNaN(converted)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < converted; i++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node

const arg = process.argv[2];

const converted = parseInt(arg);

if (isNaN(converted)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < converted; i++) {
    let row = '';
    for (let j = 0; j < converted; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

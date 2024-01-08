#!/usr/bin/node

const no1 = process.argv[2];
const no2 = process.argv[3];
const n1 = parseInt(no1);
const n2 = parseInt(no2);

const result = add(n1, n2);

console.log(result);

function add (a, b) {
  return a + b;
}

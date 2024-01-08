#!/usr/bin/node

const x = process.argv[2];

const converted = parseInt(x);

console.log(factorial(converted));

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

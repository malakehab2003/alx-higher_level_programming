#!/usr/bin/node

const x = process.argv;

if (x.length < 4) {
  console.log(0);
} else {
  let arr = [];
  for (let i = 2; i < x.length; i++) {
    arr.push(parseInt(x[i]));
  }
  let max = 0;
  for (let i = 0; i < 2; i++) {
    max = arr[0];
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] > max) {
        max = arr[j];
      }
    }
    if (i === 0) {
      arr = arr.filter(item => item !== max);
    }
  }
  console.log(max);
}

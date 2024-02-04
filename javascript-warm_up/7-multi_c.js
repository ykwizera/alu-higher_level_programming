#!/usr/bin/node

const [, , ...args] = process.argv;
if (Number(args[0])) {
  const num = parseFloat(args[0]);
  for (let i = 0; i < num.toFixed(0); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

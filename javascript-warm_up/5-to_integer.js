#!/usr/bin/node

const [, , ...args] = process.argv;

if (args.length === 1) {
  const num = parseFloat(args[0]);
  if (!isNaN(num)) {
    console.log('My number:', num.toFixed(0));
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}

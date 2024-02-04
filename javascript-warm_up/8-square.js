#!/usr/bin/node

const [, , ...args] = process.argv;
if (Number(args[0])) {
  const num = parseFloat(args[0]);
  const a = num.toFixed(0);
  for (let i = 0; i < a; i++) {
    let y = '';
    for (let z = 0; z < a; z++) {
      y += 'X';
    }
    console.log(y);
  }
} else {
  console.log('Missing size');
}

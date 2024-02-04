#!/usr/bin/node

const [, , ...args] = (process.argv);
function add(a, b) {
  const total = Number(a) + Number(b);
  return total
}
if (args[1]) {
  const sum = add(args[0], args[1])
  console.log(sum);
} else {
  console.log('NaN');
}

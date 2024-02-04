#!/usr/bin/node
const [, , ...args] = process.argv;
const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let i = 0;

do {
  console.log(myArray[i]);
  i++;
} while (i < 3);

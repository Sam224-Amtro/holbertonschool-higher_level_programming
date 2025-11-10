#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}

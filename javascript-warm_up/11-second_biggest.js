#!/usr/bin/node

const list = process.argv.slice(2).map(Number);

if (list.length <= 1) {
  console.log(0);
} else {
  const sorted = list.sort((a, b) => b - a);
  console.log(sorted[1]);
}

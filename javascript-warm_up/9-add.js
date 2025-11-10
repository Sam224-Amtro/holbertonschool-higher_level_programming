#!/usr/bin/node

const k = parseInt(process.argv[2]);
const l = parseInt(process.argv[3]);

if (isNaN(k) || isNaN(l)) {
  console.log('NaN');
} else {
  console.log(k + l);
}

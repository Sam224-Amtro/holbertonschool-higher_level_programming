#!/usr/bin/node
// process.argv[0] -> node executable path
// process.argv[1] -> script file path
// process.argv[2] -> first argument passed

const arg = process.argv[2]; // Safe: no .length used

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}

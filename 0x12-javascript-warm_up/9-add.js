#!/usr/bin/node
const args = parseInt(process.argv[2]);
const args2 = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(args, args2));

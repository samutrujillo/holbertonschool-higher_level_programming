#!/usr/bin/node
const sizeSquare = parseInt(process.argv[2]);
if (isNaN(sizeSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeSquare; i += 1) {
    console.log('X'.repeat(sizeSquare));
  }
}

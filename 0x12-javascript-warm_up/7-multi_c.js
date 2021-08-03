#!/usr/bin/node
const timeOfX = parseInt(process.argv[2]);
if (isNaN(timeOfX)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < timeOfX; i += 1) {
    console.log('C is fun');
  }
}

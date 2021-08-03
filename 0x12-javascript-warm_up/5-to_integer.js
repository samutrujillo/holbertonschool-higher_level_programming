#!/usr/bin/node
const convertArgs = parseInt(process.argv[2]);
if (isNaN(convertArgs)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertArgs);
}

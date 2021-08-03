#!/usr/bin/node
const result = process.argv.length;
console.log(result === 2 ? 'No argument' : result === 3 ? 'Argument found' : 'Arguments found');

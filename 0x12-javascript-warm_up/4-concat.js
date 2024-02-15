#!/usr/bin/node

// Extract the two arguments using process.argv
const argument1 = process.argv[2] || 'undefined';
const argument2 = process.argv[3] || 'undefined';

console.log(`${argument1}  is ${argument2}`);

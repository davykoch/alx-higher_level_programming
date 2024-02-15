#!/usr/bin/node

// Extract the first argument using process.argv
const firstArgument = process.argv[2];

// Convert the first argument to an integer using parseInt
const integerValue = parseInt(firstArgument);

console.log(isNaN(integerValue) ? 'Not a number' : `My number: ${integerValue}`);

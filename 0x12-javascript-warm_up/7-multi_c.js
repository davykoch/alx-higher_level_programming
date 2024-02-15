#!/usr/bin/node

// Extract the first argument using process.argv
const numberOfOccurrences = process.argv[2];

// Convert the first argument to an integer using parseInt
const num = parseInt(numberOfOccurrences);

// Check if the conversion is successful
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}

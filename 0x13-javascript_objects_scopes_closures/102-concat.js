#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

// Extract file paths from command line arguments
const [, , file1, file2, destination] = process.argv;

// Read the contents of the first file
const content1 = fs.readFileSync(file1, 'utf8');

// Read the contents of the second file
const content2 = fs.readFileSync(file2, 'utf8');

// Concatenate the contents of the two files
const result = content1 + content2;

// Write the result to the destination file
fs.writeFileSync(destination, result);

console.log(`Concatenated ${file1} and ${file2} into ${destination}`);

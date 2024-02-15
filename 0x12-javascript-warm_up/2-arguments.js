#!/usr/bin/node

// Check the number of arguments using process.argv
const numberOfArguments = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script name

if (numberOfArguments === 0) {
  console.log('No argument');
} else if (numberOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

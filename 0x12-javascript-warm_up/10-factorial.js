#!/usr/bin/node
function factorial (n) {
  // Base case: factorial of NaN is 1
  if (isNaN(n)) {
    return 1;
  }

  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }

  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}

const arg = process.argv[2];

console.log(factorial(parseInt(arg)));

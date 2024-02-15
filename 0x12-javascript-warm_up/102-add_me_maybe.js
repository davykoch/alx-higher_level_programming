#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// Export the addMeMaybe function for visibility from outside
module.exports.addMeMaybe = addMeMaybe;

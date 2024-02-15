#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function for visibility from outside
module.exports.callMeMoby = callMeMoby;

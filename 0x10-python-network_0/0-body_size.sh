#!/bin/bash
# This script takes a URL as input, sends a request using curl, and displays the size of the response body in bytes.
curl -sI "$1" |  grep Content-Length | cut -d ":" -f 2 | cut -d " " -f 2

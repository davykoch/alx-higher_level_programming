#!/bin/bash
# This script takes a URL as input, sends a request using curl, and displays the size of the response body in bytes.

URL=$1
SIZE=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
if [[ -z "$SIZE" ]]; then
    echo "Unable to retrieve the size of the response body for $URL"
else
    echo "Size of the response body: $SIZE bytes"
fi

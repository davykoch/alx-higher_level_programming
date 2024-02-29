#!/bin/bash
# Script Description: Sends a request to a URL using curl and displays the size of the response body in bytes

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request and display the size of the response body in bytes
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r\n'

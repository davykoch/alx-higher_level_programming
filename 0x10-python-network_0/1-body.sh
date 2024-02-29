#!/bin/bash
# Script Description: Sends a GET request to a URL using curl and displays the body of the response for a 200 status code.
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1"

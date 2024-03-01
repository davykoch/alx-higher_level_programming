#!/bin/bash
# Script Description: Sends a JSON POST request to a URL using curl with the contents of a file in the body.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

#!/bin/bash
# Script Description: Sends a GET request to a URL using curl with a custom header and displays the body of the response.
curl -s -H "X-School-User-Id: 98" "$1"

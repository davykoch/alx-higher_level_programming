#!/bin/bash
# Script Description: Sends a request to a URL using curl and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"

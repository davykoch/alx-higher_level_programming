#!/bin/bash
# Script Description: Displays all HTTP methods the server will accept for a given URL.
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'

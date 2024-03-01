#!/bin/bash
# Script Description: Displays all HTTP methods the server will accept for a given URL.
curl -s -i -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-

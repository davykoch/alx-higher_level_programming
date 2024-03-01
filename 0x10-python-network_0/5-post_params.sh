#!/bin/bash
# Script Description: Sends a POST request to a URL using curl with specified parameters and displays the body of the response.
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"

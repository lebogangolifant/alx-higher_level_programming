#!/bin/bash
# Bash script sends a POST request to the URL
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

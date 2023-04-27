#!/bin/bash
# This script sends a post request with some data to a url
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

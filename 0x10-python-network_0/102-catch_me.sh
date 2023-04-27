#!/bin/bash
# This script sends a request to a url and causes the server o respond with a string
curl -s 0.0.0.0:5000/catch_me -o /dev/null -w 'You got me!\n'

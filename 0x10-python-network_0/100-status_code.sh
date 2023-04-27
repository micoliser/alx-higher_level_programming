#!/bin/bash
# This script sends a request and displays the response status code
curl -sI "$1" | grep -E "HTTP/" | cut -d " " -f 2

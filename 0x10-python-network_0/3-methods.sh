#!/bin/bash
# This script sends a request and displays all HTTP methods accepted
curl -sIX OPTIONS "$1" | grep -E "Allow: " | cut -d " " -f 2-

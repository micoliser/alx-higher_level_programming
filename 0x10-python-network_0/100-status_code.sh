#!/bin/bash
# This script sends a request and displays the response status code
curl -so /dev/null -w %{http_code} "$1"

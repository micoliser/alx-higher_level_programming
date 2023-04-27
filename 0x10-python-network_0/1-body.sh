#!/bin/bash
# This script semds a request to a url and displays the response
curl -so /dev/null -w %{http_code} "$1" | grep -F 200 > /dev/null && curl -s "$1"

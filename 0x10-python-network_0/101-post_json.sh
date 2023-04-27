#!/bin/bash
# This script sends a post request with a json passed argument
curl -sX POST -H "Content-Type: application/json" -d "$(cat $2)" "$1"

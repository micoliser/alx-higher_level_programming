#!/bin/bash
# This script sends a post request with a json passed argument
curl -sX POST -json @"$2" "$1"

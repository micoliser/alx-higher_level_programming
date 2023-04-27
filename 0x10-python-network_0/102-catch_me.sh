#!/bin/bash
# This script sends a request to a url and causes the server o respond with a string
curl -sLX PUT 0.0.0.0:5000/catch_me_2 -H "Origin: School" -d "user_id=98"

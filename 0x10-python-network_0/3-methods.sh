#!/bin/bash
# Bash script to print out all allowed methods in http response
curl -si 0.0.0.0:5000/route_4 | grep 'Allow' | awk -F ":"  '{print $2}'

#!/bin/bash
# Bash script to print out all allowed methods in http response
curl -sI $1 | grep 'Allow' | awk -F ": "  '{print $2}'

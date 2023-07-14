#!/bin/bash
# Selecting only content length header from curl response
curl -sI $1 | grep Content-Length: | awk '{print $2}'

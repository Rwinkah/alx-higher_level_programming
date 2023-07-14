#!/bin/bash
# Selecting only content length header from curl response

curl -sI localhost | grep Content-Length: | awk '{print $2}'

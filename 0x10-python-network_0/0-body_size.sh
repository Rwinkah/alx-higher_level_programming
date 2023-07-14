#!/usr/bin/env bash
# Selecting only content length header from curl response

 curl -sI localhost | grep Content-Length: | grep -o '[0-9]\+'

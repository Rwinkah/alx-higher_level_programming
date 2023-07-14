#!/bin/bash
# bash script to send a get request containing a custom header
curl -H "X-School-User-Id: 98" -s $1

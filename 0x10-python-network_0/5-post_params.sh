#!/bin/bash
# bash script to send a  post request with curl
curl -X POST -d "email=test@gmail.com&subject='I will always be here for PLD'" -s $1

#!/bin/bash
# print the status of the code
curl -s -o /dev/null -w "%{http_code}" "$1"

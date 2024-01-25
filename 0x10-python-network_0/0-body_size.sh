#!/bin/bash
# get content size
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s "$1" | wc -c

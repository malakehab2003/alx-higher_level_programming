#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep -i allow | cut -d ' ' -f 2-

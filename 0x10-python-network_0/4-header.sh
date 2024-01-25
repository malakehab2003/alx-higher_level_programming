#!/bin/bash
# GET request to the URL, A header variable X-School-User-Id must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"

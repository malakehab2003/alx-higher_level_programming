#!/bin/bash
# get content size
curl -s "$1" | wc -c

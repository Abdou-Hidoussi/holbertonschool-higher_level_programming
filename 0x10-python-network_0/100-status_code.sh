#!/bin/bash
# Task 100
curl -sSL -D - "%{http_code}" "$1" -o /dev/null

#!/bin/bash
# Task 100
curl -s -w "%{http_code}" "$1" -o /dev/null

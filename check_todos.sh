#!/bin/bash
#TODO: Make this Work
find ./ -type f -exec cat {} + | grep 'TODO:' | cut -d '#' -f2 | tr -d '\t'
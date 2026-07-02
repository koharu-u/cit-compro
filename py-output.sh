#!/usr/bin/env bash
mkdir -p output
python3 "$1" > "output/$(basename "$1" .py).output"

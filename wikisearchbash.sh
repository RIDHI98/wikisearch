#!/bin/sh
if [[ -z "$1" ]]; then
  echo "Enter your word"
  read word
elif [[ -n "$1" ]]; then
  word="$*"
fi

word="${word// /_}"

echo "...looking for $word..."

link="https://en.wikipedia.org/wiki/$word"

echo "$link"
destdir=log.txt
echo "${link}" >> "$destdir"

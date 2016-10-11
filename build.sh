#!/bin/bash
. ./env.sh

echo "Docker build settings:"
echo "- Container Name: $CONTAINERNAME"
echo ""
echo "Starting Docker build..."

docker build -t "$CONTAINERNAME" .
if [ $? -eq 0 ]; then
  echo "SUCCESS."
else
  echo "FAILED."
fi

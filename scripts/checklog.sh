#!/bin/bash
cd "$(dirname "$0")"
. ../env.sh

echo "Connecting to $SERVICENAME:$LOG_FILE..."
docker exec -it $SERVICENAME tail -f $LOG_FILE 

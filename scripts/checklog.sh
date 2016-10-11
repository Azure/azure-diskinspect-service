#!/bin/bash
. ../env.sh

echo "Connecting to $SERVICENAME:$LOG_FILE..."
docker exec -it $SERVICENAME tail -f $LOG_FILE 

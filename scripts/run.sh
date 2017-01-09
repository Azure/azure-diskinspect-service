#!/bin/bash
cd "$(dirname "$0")"
. ../env.sh

echo "Cleaning up previous instances..."
docker stop $SERVICENAME
docker rm -f $SERVICENAME
docker rm -f $SERVICEVOLUMENAME

if [ ! -f $SSL_PRIVATE_KEY ]
then
  echo "File $SSL_PRIVATE_KEY is missing."
  exit 1
fi
if [ ! -f $SSL_PUBLIC_KEY ]
then
  echo "File $SSL_PUBLIC_KEY is missing."
  exit 1
fi

echo "Starting service..."
docker create -v /etc/nginx/ssl --name $SERVICEVOLUMENAME ubuntu
docker cp $SSL_PATH/. $SERVICEVOLUMENAME:/etc/nginx/ssl/.
docker run -h $CONTAINERHOSTNAME --restart unless-stopped -t -d -p 8080:8080 --name $SERVICENAME --volumes-from $SERVICEVOLUMENAME -e affinity:image==$CONTAINERNAME $CONTAINERNAME
echo "Done."

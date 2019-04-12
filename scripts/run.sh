#!/bin/bash
cd "$(dirname "$0")"
. ../env.sh

az_registry=$1
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

if [ $TRAVIS ]; then
  docker pull $az_registry/$CONTAINERREPO
  CONTAINERNAME=$az_registry/$CONTAINERREPO
  CONTAINERTAG="latest"
fi

echo "Starting service..."
docker create -v /etc/nginx/ssl --name $SERVICEVOLUMENAME ubuntu
docker cp $SSL_PATH/. $SERVICEVOLUMENAME:/etc/nginx/ssl/.

if docker container inspect -f . $CREDSCANSERVICEVOLUMENAME; then
  echo "Running with Credential Scanner"
  docker run -h $CONTAINERHOSTNAME --restart unless-stopped -t -d -p 8080:8080 --name $SERVICENAME --volumes-from $SERVICEVOLUMENAME --volumes-from $CREDSCANSERVICEVOLUMENAME -e APPINSIGHTS_KEY=$APPINSIGHTS_KEY -e CONTAINER_VERSION=$CONTAINERTAG -e affinity:image==$CONTAINERNAME $CONTAINERNAME   
else
  docker run -h $CONTAINERHOSTNAME --restart unless-stopped -t -d -p 8080:8080 --name $SERVICENAME --volumes-from $SERVICEVOLUMENAME -e APPINSIGHTS_KEY=$APPINSIGHTS_KEY -e CONTAINER_VERSION=$CONTAINERTAG -e affinity:image==$CONTAINERNAME $CONTAINERNAME
fi

echo "Done."

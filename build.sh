#!/bin/bash 
. ./env.sh

echo "Docker build settings:"
echo "- Container Name: $CONTAINERNAME"
echo ""
echo "Starting Docker build..."


file_output=$1
if [ -z $file_output ]; then
	file_output="~/docker_build.txt"
fi
echo "Redirecting to $file_output"
#handle expansion of environment variables
file_output=$(eval echo $file_output)
docker build -t "$CONTAINERNAME" . > $file_output
if [ $? -eq 0 ]; then
  echo "SUCCESS."
else
  echo "FAILED."
fi

if  [ ! $TRAVIS ] && [ ! -f $HOME/azdis_ssl/azdis_private.rsa ]; then   
  mkdir $HOME/azdis_ssl
  openssl req -x509 -newkey rsa:2048 -keyout $HOME/azdis_ssl/azdis_private.rsa -out $HOME/azdis_ssl/azdis_public.crt -days 365 -nodes -subj "/CN=localhost"
fi

if [ $TRAVIS ]; then
  docker tag $CONTAINERNAME $CONTAINERREGISTRY/$CONTAINERREPO
  docker push $CONTAINERREGISTRY/$CONTAINERREPO
fi
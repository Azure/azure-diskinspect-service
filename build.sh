#!/bin/bash 
. ./env.sh

echo "Docker build settings:"
echo "- Container Name: $CONTAINERNAME"
echo ""
echo "Starting Docker build..."
echo "Github actions env: $GITHUB_ACTIONS"
if [ $GITHUB_ACTIONS ]; then
  echo "Github actions true"
else
  echo "fasle"
fi


file_output=$1
az_registry=$2
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

if  [ ! $TRAVIS || ! $GITHUB_ACTIONS ] && [ ! -f $HOME/azdis_ssl/azdis_private.rsa ]; then   
  mkdir $HOME/azdis_ssl
  openssl req -x509 -newkey rsa:2048 -keyout $HOME/azdis_ssl/azdis_private.rsa -out $HOME/azdis_ssl/azdis_public.crt -days 365 -nodes -subj "/CN=localhost"
fi

if [ $TRAVIS || $GITHUB_ACTIONS ]; then
  docker tag $CONTAINERNAME $az_registry/$CONTAINERREPO
  docker push $az_registry/$CONTAINERREPO
fi

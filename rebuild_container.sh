#!/bin/bash
IMAGE_TAG="jmanzur/crud_api"
IMAGE_NAME="CRUD_API"

read -p "This script will stop and remove the docker container $IMAGE_NAME. do you wish to continue (y/n)? " -n 1 -r
echo -e '\n'
if [[ $REPLY =~ ^[Yy]$ ]]
    then
        echo "Stopping and removing the $IMAGE_NAME container"
        echo -e '\n'
        docker stop $IMAGE_NAME && docker rm $IMAGE_NAME
        echo -e '\n'
        echo "Removing the $IMAGE_TAG image"
        echo -e '\n'
        docker image rm $(docker images --filter=reference=$IMAGE_TAG --format "{{.ID}}")
        echo -e '\n'
        echo "Building the new $IMAGE_TAG image and running the new $IMAGE_NAME container"
        echo -e '\n'
        docker build -t $IMAGE_TAG . && docker run -d -p 8082:8082 --name $IMAGE_NAME $IMAGE_TAG
        echo -e '\n'
        exit 0
    else
        echo "The process was canceled by the user."
        echo -e '\n'
		exit 0
fi


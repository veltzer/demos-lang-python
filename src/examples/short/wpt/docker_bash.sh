#!/usr/bin/bash

# run bash on a container, given the image name of the containr

image_name=$1
id=$(docker ps --filter "ancestor=$image_name" --format "{{.ID}}")
docker exec -it "$id" bash

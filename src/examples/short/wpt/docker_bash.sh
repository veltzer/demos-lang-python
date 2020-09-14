#!/usr/bin/bash

# run bash on a container


id=`docker ps -q`
docker exec -it "$id" bash

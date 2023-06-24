#!/bin/sh
NAME="elasticsearch:8.8.1"
docker rm $(docker stop $(docker ps -a -q --filter ancestor="${NAME}" --format="{{.ID}}"))

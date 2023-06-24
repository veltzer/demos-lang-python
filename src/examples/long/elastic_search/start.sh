#!/bin/sh

# start up a single node elastic search for local development
# References:
# - https://levelup.gitconnected.com/how-to-run-elasticsearch-8-on-docker-for-local-development-401fd3fff829
NAME="elasticsearch:8.8.1"
sudo sysctl -w vm.max_map_count=262144
docker run\
	-p 9200:9200\
	--name elastic\
	--detach\
	-e ES_JAVA_OPTS="-Xms1g -Xmx1g"\
	-e discovery.type=single-node\
	-e xpack.security.enabled=false\
	"${NAME}"
# --network host\

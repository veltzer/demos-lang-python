#!/bin/sh
NAME="elasticsearch:8.8.1"
sudo sysctl -w vm.max_map_count=262144
docker run\
	-p 9200:9200\
	--detach\
	-e ES_JAVA_OPTS="-Xms1g -Xmx1g"\
	-e discovery.type=single-node\
	-e xpack.security.enabled=false\
	"${NAME}"
# --network host\

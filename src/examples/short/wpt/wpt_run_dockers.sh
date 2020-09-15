#!/usr/bin/bash

docker_kill_all_and_remove.sh
echo "running the web server..."
# server is listening on port 80
docker run -d --network host webpagetest/server
echo "sleeping for 5 seconds to let the server boot up..."
sleep 5
echo "running the web agent..."
# redirect agent to port 81 to not collide with the web server 80 port
docker run\
	-d\
	--network host\
	--cap-add=NET_ADMIN\
	-e "SERVER_URL=http://localhost:80/work/"\
	-e "LOCATION=Test"\
	-e "--dockerized"\
	webpagetest/agent

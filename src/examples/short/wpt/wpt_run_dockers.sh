#!/usr/bin/bash

<<COMMENT

This script runs two dockers that together make up a whole webpagetest
system: a server and an agent. They talk to each other via http and that's
why we connect both of them to the hosts network (so they could find each
other easily). We also pass the the addess of the server to the agent
so that he could find it.

The weirdest thing here is the --cap-add=NET_ADMIN flag to docker for the
agent container. This is because the agent code tries to do traffic shaping
or throtteling via the network configuration even if you tell wegpagetest
not to do traffic shaping at all (!). This means that it has to have the
capability NET_ADMIN. This was hard to find.

COMMENT

echo "running the web server..."
docker run -d --network host webpagetest/server
echo "sleeping for 5 seconds to let the server boot up..."
sleep 5
echo "running the web agent..."
docker run\
	-d\
	--network host\
	--cap-add=NET_ADMIN\
	-e "SERVER_URL=http://localhost/work/"\
	-e "LOCATION=Test"\
	webpagetest/agent

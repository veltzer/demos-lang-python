 #!/usr/bin/bash

# docker run -d -p 80:80 -p 443:443 webpagetest/server
docker run -d --network host webpagetest/server

# Client Server Using Twisted

Write a TCP server using twisted. It should listen on port 2345
and should implement the following protocol:

c- client
s- server

c:Hello (on error - close connection)
s:Hello
c:Auth,[username],[pass]
s: checks user,passed (if password!=user+user says bye and closes connection)
c:getStatus
s:sends internal status (add number of current connected users)
c:bye
s:closes connection

## Extra credit
add client option to request the server to listen on a new port
Example:
c: startListening,3100,Hello
From this point on server listens on port 3100 and says "Hello"
on any input...

## Extra extra credit
Client can send NEW CODE to be executed on the server (a major
security no no).

import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:1234")

# Send a "message" using the socket
for request in range(0,10001):
    sock.send(str(request).encode())
    print("Message pushed, input = " + str(request))
    #print(sock.recv().decode())
    #sock.send("Hello".encode())
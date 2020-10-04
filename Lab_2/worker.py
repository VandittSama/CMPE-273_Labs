import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:1234")

sock2 = context.socket(zmq.PUSH)
sock2.connect("tcp://127.0.0.1:1235")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    message = message.decode()
    print("Message pulled, input = " + str(message))
    reply_msg = "Square root of " + message + " is " + str(int(message) ** 0.5)
    sock2.send(str(reply_msg).encode())
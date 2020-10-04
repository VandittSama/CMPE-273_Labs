import zmq

# Setup ZMQ socket.
context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.bind("tcp://127.0.0.1:1235")

# Accumulate the results until we know all computations are done.
results = []
num_processed = 0
while True:
    result = sock.recv()
    result = result.decode()
    print(result)
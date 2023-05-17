# server .py
import atexit
import socket
import time

print("Running server.....")
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)


# establish a connection

# Close socket when exit
@atexit.register
def handler():
    serversocket.close()


while True:
    sock, addr = serversocket.accept()
    print(f"Connected with {addr[0]}, {addr[1]}")
    currentTime = f"Traveler datang pada waktu {time.ctime(time.time())}"
    sock.send(currentTime.encode('ascii'))
    sock.close()

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)
print('Server is listening on {}:{}'.format(*server_address))

while True:
    print('Menunggu client connect...')
    client_socket, client_address = server_socket.accept()
    print('Connected to client:', client_address)

    data = client_socket.recv(1024).decode()
    print('Received data:', data)

    response = data.upper()

    client_socket.sendall(response.encode())

    client_socket.close()
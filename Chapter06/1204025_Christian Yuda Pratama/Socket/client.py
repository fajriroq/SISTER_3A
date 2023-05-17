import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)
print('Koneksi ke server:', server_address)

message = input('Masukkan pesan yang akan dikirimkan ke server: ')

client_socket.sendall(message.encode())

response = client_socket.recv(1024).decode()
print('Respon Server:', response)

client_socket.close()

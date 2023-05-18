import socket

# Membuat objek socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan socket ke server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("Connected to", server_address)

while True:
    # Mengirim data ke server
    message = input("Client: ")
    client_socket.send(message.encode())

    # Memeriksa jika client ingin keluar
    if message.lower() == 'exit':
        break

    # Menerima respon dari server
    response = client_socket.recv(1024).decode()
    print("Server:", response)

# Menutup koneksi
client_socket.close()

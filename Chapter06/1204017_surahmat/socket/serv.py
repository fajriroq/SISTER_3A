import socket

# Membuat objek socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengikat (bind) socket ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(1)

print("Server listening on", server_address)

# Menerima koneksi dari klien
client_socket, client_address = server_socket.accept()
print("Connected to", client_address)

while True:
    # Menerima data dari klien
    data = client_socket.recv(1024).decode()
    print("Client:", data)

    # Memeriksa jika klien ingin keluar
    if data.lower() == 'exit':
        break

    # Mengirim balasan ke klien
    response = input("Server: ")
    client_socket.send(response.encode())

# Menutup koneksi
client_socket.close()
server_socket.close()

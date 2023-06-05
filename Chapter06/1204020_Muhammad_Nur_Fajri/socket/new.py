import socket

# Inisialisasi alamat IP dan port
IP = '127.0.0.1'
PORT = 1234

# Membuat socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengikat socket ke alamat IP dan port
server_socket.bind((IP, PORT))

# Mendengarkan koneksi masuk
server_socket.listen(1)

print(f"Server listening on {IP}:{PORT}")

# Menerima koneksi dari client
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

while True:
    # Menerima data dari client
    data = client_socket.recv(1024).decode('utf-8')

    if not data:
        # Jika tidak ada data, berarti koneksi telah ditutup oleh client
        print("Connection closed by client")
        break

    print(f"Received data: {data}")
    if data == "-V":
        ver = "Tuhan_baru 2.0"
        client_socket.send(ver.encode('utf-8'))
    # Mengirim balasan ke client
    response = "respon ke server baru sucessfully"
    client_socket.send(response.encode('utf-8'))

# Menutup socket
server_socket.close()

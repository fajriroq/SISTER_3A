import socket

# Inisialisasi alamat IP dan port
IP = '127.0.0.1'
PORT = 1234

# Membuat socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mencoba terhubung ke server
client_socket.connect((IP, PORT))
print("Connected to server")

while True:
    # Meminta input dari pengguna
    message = input("Enter a message (or 'exit' to quit): ")

    if message == 'exit':
        break

    # Mengirim data ke server
    client_socket.send(message.encode('utf-8'))

    # Menerima balasan dari server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

# Menutup socket
client_socket.close()

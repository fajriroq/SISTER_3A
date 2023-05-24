import socket
import json

# Membuat socket object
s = socket.socket()
host = socket.gethostname()
port = 60000
s.connect((host, port))
print('Terhubung dengan server')

# Mengirim pesanan ke server
order = input("Masukkan nomor item yang ingin dipesan (pisahkan dengan koma): ")
s.send(order.encode())

# Menerima respon dari server
response = s.recv(1024).decode()

# Menguraikan respon JSON
response_data = json.loads(response)

# Menampilkan pesanan dan total harga
if response_data["items"]:
    print("Pesanan Anda:")
    for item in response_data["items"]:
        print("- %s: Rp %d" % (item["nama"], item["harga"]))
    print("Total: Rp %d" % response_data["total"])
else:
    print("Tidak ada pesanan.")

# Menutup koneksi dengan server
s.send(b'Terima kasih')
s.close()
print('Koneksi ditutup')

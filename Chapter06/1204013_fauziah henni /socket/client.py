import socket
import json

# Membuat socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mendapatkan nama mesin lokal
host = socket.gethostname()
port = 9999

# Menghubungkan ke server
s.connect((host, port))
print("Terhubung dengan server")

# Mengirim pesanan ke server
order = input("Masukkan nomor item yang ingin dipesan (pisahkan dengan koma): ")
s.send(order.encode('utf-8'))

# Menerima respon dari server
response = s.recv(1024).decode('utf-8')

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
s.close()


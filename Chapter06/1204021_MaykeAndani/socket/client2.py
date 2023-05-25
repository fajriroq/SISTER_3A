import socket
import json

# Membuat socket object
s = socket.socket()
host = socket.gethostname()
port = 60000
s.connect((host, port))
print('Terhubung dengan server')

# Mengirim permintaan informasi karyawan ke server
request = input("Masukkan nomor karyawan yang ingin dilihat (pisahkan dengan koma): ")
s.send(request.encode())

# Menerima respon dari server
response = s.recv(1024).decode()

# Menguraikan respon JSON
response_data = json.loads(response)

# Menampilkan informasi karyawan
if response_data["karyawan"]:
    print("Informasi Karyawan:")
    for karyawan in response_data["karyawan"]:
        print("- Nama: %s" % karyawan["nama"])
        print("  Usia: %d" % karyawan["usia"])
        print("  Posisi: %s" % karyawan["posisi"])
else:
    print("Tidak ada karyawan dengan nomor yang diminta.")

# Menutup koneksi dengan server
s.send(b'Terima kasih')
s.close()
print('Koneksi ditutup')

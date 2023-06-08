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

# Mengirim permintaan informasi karyawan ke server
request = input("Masukkan nomor karyawan yang ingin dilihat (pisahkan dengan koma): ")
s.send(request.encode('utf-8'))

# Menerima respon dari server
response = s.recv(1024).decode('utf-8')

# Menguraikan respon JSON
response_data = json.loads(response)

# Menampilkan informasi karyawan
print("Informasi Karyawan:")
for karyawan in response_data["karyawan"]:
    print("- Nama: %s" % karyawan["nama"])
    print("  Usia: %d" % karyawan["usia"])
    print("  Posisi: %s" % karyawan["posisi"])
    print("  Gaji: %s" % karyawan["gaji"])
    print("  Masa Jabatan: %s" % karyawan["masa_jabatan"])    
        


# Menutup koneksi dengan server
s.close()

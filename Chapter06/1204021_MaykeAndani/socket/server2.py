import socket
import json

# Membuat data karyawan
karyawan = [
    {"nama": "John Doe", "usia": 25, "posisi": "Staff"},
    {"nama": "Jane Smith", "usia": 30, "posisi": "Manager"},
    {"nama": "Mike Johnson", "usia": 35, "posisi": "Supervisor"},
    {"nama": "Sarah Lee", "usia": 28, "posisi": "Staff"},
    {"nama": "David Brown", "usia": 32, "posisi": "Manager"}
]

# Membuat socket object
s = socket.socket()
port = 60000
host = socket.gethostname()
s.bind((host, port))
s.listen(15)
print('Server listening....')

# Fungsi untuk memproses permintaan informasi karyawan dari klien
def process_request(request):
    request_items = request.split(",")  # Permintaan dikirim sebagai string terpisah oleh koma
    requested_karyawan = []

    for item in request_items:
        item = int(item)
        if item >= 0 and item < len(karyawan):
            requested_karyawan.append(karyawan[item])

    return requested_karyawan

# Menerima koneksi dan memproses permintaan informasi karyawan
while True:
    conn, addr = s.accept()
    print('Terhubung dengan', addr)

    # Menerima permintaan informasi karyawan dari klien
    request = conn.recv(1024).decode()
    print('Server menerima', repr(request))

    # Memproses permintaan informasi karyawan
    requested_karyawan = process_request(request)

    # Mengirimkan respon ke klien
    response = {"karyawan": requested_karyawan}
    conn.send(json.dumps(response).encode())

    # Menutup koneksi dengan klien
    conn.send(b'->Thank you for connecting')
    conn.close()

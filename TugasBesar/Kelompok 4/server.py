import socket
import json

# Membuat data karyawan
karyawan = [
    {"nama": "Mayke Andani", "usia": 22, "posisi": "Staff", "gaji": 5000000, "masa_jabatan": "2 tahun"},
    {"nama": "Wulan Nur", "usia": 21, "posisi": "Staff", "gaji": 6000000, "masa_jabatan": "2 tahun"},
    {"nama": "Nurul", "usia": 30, "posisi": "Manager", "gaji": 5000000, "masa_jabatan": "5 tahun"},
    {"nama": "Fauziah", "usia": 35, "posisi": "Supervisor", "gaji": 4500000, "masa_jabatan": "3 tahun"},
    {"nama": "Rama", "usia": 28, "posisi": "Staff", "gaji": 3200000, "masa_jabatan": "1 tahun"},
    {"nama": "Sinta", "usia": 32, "posisi": "Manager", "gaji": 4800000, "masa_jabatan": "4 tahun"}
]

# Membuat socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mendapatkan nama mesin lokal
host = socket.gethostname()
port = 9999

# Bind ke port
serversocket.bind((host, port))

# Mendengarkan hingga 5 permintaan
serversocket.listen(5)
print("Server sedang berjalan...")

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
    clientsocket, addr = serversocket.accept()
    print("Terhubung dengan %s" % str(addr))

    # Menerima permintaan informasi karyawan dari klien
    request = clientsocket.recv(1024).decode('utf-8')

    # Memproses permintaan informasi karyawan
    requested_karyawan = process_request(request)

    # Mengirimkan respon ke klien
    response = {"karyawan": requested_karyawan}
    clientsocket.send(json.dumps(response).encode('utf-8'))

    # Menutup koneksi dengan klien
    clientsocket.close()

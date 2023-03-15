import socket
import time
import struct
import os

# Mendefinisikan alamat server NTP dan port
ntp_server_address = ('pool.ntp.org', 123)

# Mengirim permintaan waktu ke server NTP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = b'\x1b' + 47 * b'\0'
client.sendto(message, ntp_server_address)

# Menerima waktu dari server NTP
data, server = client.recvfrom(1024)
if data:
    # Mengubah data waktu menjadi nilai float
    ntp_time = struct.unpack('!12I', data)[10]
    # Menghitung selisih waktu antara waktu sistem dengan waktu dari server NTP
    delta_time = ntp_time - time.time()
    # Menyesuaikan waktu sistem dengan waktu dari server NTP
    new_time = time.time() + delta_time
    # Mengatur waktu sistem menggunakan waktu yang sudah disesuaikan
    os.system('date -s @' + str(int(new_time)))

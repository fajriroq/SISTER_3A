import ntplib
import time
from time import ctime

# Menentukan server waktu
ntp_server = 'pool.ntp.org'

# Membuat koneksi dengan server
client = ntplib.NTPClient()
response = client.request(ntp_server)

# Mengatur waktu sistem dengan waktu dari server NTP
print("Waktu sebelum disinkronisasi: ", ctime())
def calculate_average_time(time_list):
    return sum(time_list) / len(time_list)

def run_cristian_algorithm():
    # Melakukan beberapa pengukuran waktu
    time_list = []
    for i in range(10):
        start_time = int(time.time() * 1000)
        time.sleep(0.1)
        end_time = int(time.time() * 1000)
        time_list.append((start_time + end_time) // 2)

    # Menghitung waktu rata-rata dari beberapa pengukuran waktu
    avg_time = calculate_average_time(time_list)

    # Menampilkan waktu yang telah disesuaikan
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(avg_time / 1000))
    print('Waktu sekarang setelah disesuaikan dengan algoritma Cristian: ', time_str)

# Menjalankan algoritma Cristian tanpa server
run_cristian_algorithm()


from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_QuisDadakan = 5
hasilakhir = Barrier(num_QuisDadakan)
peserta = ['ara', 'yaya', 'tiara', 'mustika', 'yara']

print("\n ### Absensi Kelas A ### \n")

def siswa():
    name = peserta.pop()
    sleep(randrange(2, 7))
    print('%s Datang ke kelas pada: %s \n' % (name, ctime()))
    hasilakhir.wait()

def main():
    threads = []
    print('Dimulai!!')
    for i in range(num_QuisDadakan):
        threads.append(Thread(target=siswa))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('selesai!')

if __name__ == "__main__":
    main()

import threading
import time

# fungsi untuk mengisi absen
print("\n ### Absensi ### \n")
import threading

# Variabel untuk menyimpan data presensi
presensi = {}

# Fungsi untuk mengecek presensi
def cek_presensi(nama):
    # Simulasi waktu yang dibutuhkan untuk mengecek presensi
    time.sleep(2)
    presensi[nama] = True
    print(f"{nama} telah melakukan presensi")

# Fungsi untuk mengecek keterlambatan peserta
def cek_keterlambatan(nama):
    # Simulasi waktu yang dibutuhkan untuk mengecek keterlambatan
    time.sleep(1)
    if nama == "Jane":
        print(f"{nama} terlambat hadir")
    else:
        print(f"{nama} hadir tepat waktu")

# Membuat objek lock untuk menghindari race condition
lock = threading.Lock()

# Fungsi untuk mengeksekusi presensi
def eksekusi_presensi(nama):
    # Mengambil objek lock
    lock.acquire()
    # Memanggil fungsi cek_keterlambatan dengan parameter nama
    cek_keterlambatan(nama)
    # Memanggil fungsi cek_presensi dengan parameter nama
    cek_presensi(nama)
    # Melepas objek lock
    lock.release()

# Membuat daftar nama peserta
daftar_nama = ['ara', 'yaya', 'tiara', 'mustika', 'yara']

# Membuat objek thread untuk setiap peserta
threads = []
for nama in daftar_nama:
    t = threading.Thread(target=eksekusi_presensi, args=(nama,))
    threads.append(t)

# Memulai eksekusi presensi dalam thread yang berbeda
for t in threads:
    t.start()

# Menunggu semua thread selesai sebelum melanjutkan ke instruksi selanjutnya
for t in threads:
    t.join()

# Menampilkan data presensi setelah semua thread selesai
print("Data Presensi:")
print(presensi)

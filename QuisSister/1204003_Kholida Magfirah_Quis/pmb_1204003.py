import threading
import time
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

print('\nSilahkan Mendaftar Terlebih Dahulu Dalam Waktu 5 Detik!\n')
def daftar_mahasiswa(nama_mahasiswa):
    global count
    print(f"Mahasiswa {nama_mahasiswa} sedang mendaftar")
    time.sleep(5) # simulasi pendaftaran
    count += 1
    print(f"Mahasiswa {nama_mahasiswa} telah selesai mendaftar")

if __name__ == "__main__":
    start_time = time.time()
    count = 0
    mahasiswa = ["Fira", "Kholida", "Magfirah", "Ani", "Ina"]

    threads = []
    for mhs in mahasiswa:
        t = threading.Thread(target=daftar_mahasiswa, args=(mhs,))
        threads.append(t)
        t.start()

    # menggunakan synchronization untuk mengontrol akses ke variabel count
    for t in threads:
        t.join()

    end_time = time.time()

    print(f"\nSemua mahasiswa telah selesai mendaftar. Total: {count}\n")
    print(f"Waktu mulai: {start_time}")
    print(f"Waktu selesai: {end_time}")
    print(f"Waktu eksekusi: {end_time - start_time}")

    print("\nMahasiswa Terlambat Mendaftar\n")

    # inisiasi object thread
    t1 = threading.Thread(target=daftar_mahasiswa, args=("Budi",))
    t2 = threading.Thread(target=daftar_mahasiswa, args=("Adit",))

    # menggunakan synchronization untuk mengontrol akses ke variabel count
    lock = threading.Lock()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Mahasiswa Budi dan Adit telah selesai mendaftar. Total: {count}")
    print("\nPendaftaran Selesai\n")
num_runners = 7
finish_line = Barrier(num_runners)
runners = ["Fira", "Kholida", "Magfirah", "Ani", "Ina","Budi","Adit"]

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s Mendaftar Pada: %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('\nUrutan Mahasiswa Mendaftar\n')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('\nSeluruh Proses Selesai!\n')

if __name__ == "__main__":
    main()

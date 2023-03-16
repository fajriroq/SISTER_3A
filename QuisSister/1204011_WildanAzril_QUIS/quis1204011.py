import threading
import time

# Membuat objek Barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(3)


class jalur:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def jalur_tentu(self):
        print(
            f"{self.nama} mulai melakukan pendaftaran pada {time.ctime(time.time())}")
        time.sleep(2)
        print(
            f"{self.nama} berhasil melakukan pendaftaran pada {time.ctime(time.time())}")
        # Thread menunggu di barier
        barrier.wait()
        print(f"{self.nama} diterima pada jalur {self.jenis}\n")


# Data jalur
jalur1 = jalur("Mahasiswa 1", "Undangan")
jalur2 = jalur("Mahasiswa 2", "Reguler")
jalur3 = jalur("Mahasiswa 3", "Beasiswa")

if __name__ == '__main__':
    # membuat thread baru untuk setiap jalur
    t1 = threading.Thread(target=jalur1.jalur_tentu)
    t1.start()

    t2 = threading.Thread(target=jalur2.jalur_tentu)
    t2.start()

    t3 = threading.Thread(target=jalur3.jalur_tentu)
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    # menampilkan pesan ketika semua jalur pendaftaran ditutup
    print("Semua jalur pendaftaran ditutup pada jam: ", time.ctime(time.time()))

    start_time = time.time()
    end_time = time.time()
    print("Perbandingan pendaftar dan penerima = ", end_time - start_time)

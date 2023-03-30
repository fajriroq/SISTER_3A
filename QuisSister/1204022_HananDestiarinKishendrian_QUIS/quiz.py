import threading
import time

# Membuat objek Barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(3)


class Tagihan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def tagihan_1(self):
        print(f"{self.nama} Terdapat tagihan pada {time.ctime(time.time())}")
        time.sleep(2)
        print(f"{self.nama} Tagihan lunas pada {time.ctime(time.time())}")
        # Thread menunggu di barier
        barrier.wait()
        print(f"{self.nama} Pembayaran tagihan {self.jenis} lunas\n")


# Daftar tagihan
tagihan1 = Tagihan("Tagihan 1", "Air pam")
tagihan2 = Tagihan("Tagihan 2", "Listrik")
tagihan3 = Tagihan("Tagihan 3", "WIFI")

if __name__ == '__main__':
    # membuat thread baru untuk setiap jalur
    t1 = threading.Thread(target=tagihan1.tagihan_1)
    t2 = threading.Thread(target=tagihan2.tagihan_1)
    t3 = threading.Thread(target=tagihan3.tagihan_1)

    # menjalankan thread
    t1.start()
    t2.start()
    t3.start()

    # menunggu thread selesai
    t1.join()
    t2.join()
    t3.join()

    # menampilkan pesan tenggang waktu pelunasan
    print("Tenggang waktu pelunasan : ", time.ctime(time.time()))

    start_time = time.time()
    time.sleep(2)  
    end_time = time.time()
    print("Perbandingan waktu tagihan dan pelunasan = ", end_time - start_time)

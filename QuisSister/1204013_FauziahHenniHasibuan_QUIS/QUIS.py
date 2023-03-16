import threading
import time

# Membuat objek Barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(3)

class Honorer:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_gaji(self):
        print(f"{self.nama} mulai perhitungan gaji pada jam {time.ctime(time.time())}")
        time.sleep(2)
        print(f"{self.nama} selesai perhitungan gaji pada jam {time.ctime(time.time())}")
        # Thread menunggu di barrier
        barrier.wait()
        print(f"{self.nama} mendapatkan gaji sebesar Rp. {self.gaji}\n")

# Data honorer
honorer1 = Honorer("Honorer 1", 3000000)
honorer2 = Honorer("Honorer 2", 2500000)
honorer3 = Honorer("Honorer 3", 4000000)

if __name__ == '__main__':
    # membuat thread baru untuk setiap honorer
    t1 = threading.Thread(target=honorer1.hitung_gaji)
    t2 = threading.Thread(target=honorer2.hitung_gaji)
    t3 = threading.Thread(target=honorer3.hitung_gaji)

    # menjalankan thread
    t1.start()
    t2.start()
    t3.start()

    # menunggu thread selesai
    t1.join()
    t2.join()
    t3.join()

    # menampilkan pesan ketika semua perhitungan gaji selesai
    print("Semua perhitungan gaji selesai pada jam: ", time.ctime(time.time()))


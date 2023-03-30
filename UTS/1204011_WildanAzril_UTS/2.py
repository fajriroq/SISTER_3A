import multiprocessing
import time

# Membuat objek Barrier dengan jumlah Process yang akan dijalankan
barrier = multiprocessing.Barrier(3)


class Barang:
    def __init__(self, nama_barang, alamat_tujuan):
        self.nama_barang = nama_barang
        self.alamat_tujuan = alamat_tujuan

    def waktu_barang(self):
        print(
            f"{self.nama_barang} mulai melakukan pengiriman pada {time.ctime(time.time())}")
        time.sleep(2)
        print(
            f"{self.nama_barang} berhasil melakukan pengiriman pada {time.ctime(time.time())}")
        # Process menunggu di barier
        print(f"{self.nama_barang} dikirim menuju ke alamat {self.alamat_tujuan}\n")


# Data Barang
barang1 = Barang("Buku", "Jl. Merdeka No.10")
barang2 = Barang("Computer", "Jl. Soekarno-Hatta N0.07")
barang3 = Barang("SmartWatch", "Sarijadi Raya No. 27")

if __name__ == '__main__':
    # membuat Process baru untuk setiap barang
    p1 = multiprocessing.Process(target=barang1.waktu_barang)
    p1.start()

    p2 = multiprocessing.Process(target=barang2.waktu_barang)
    p2.start()

    p3 = multiprocessing.Process(target=barang3.waktu_barang)
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    # menampilkan pesan ketika semua jalur pendaftaran ditutup
    print("Semua pengiriman telah selesai pada: ", time.ctime(time.time()))

    start_time = time.time()
    end_time = time.time()
    print("Perbandingan pengiriman barang = ", end_time - start_time)

import threading
import time

# Membuat objek Barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(3 )

class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def perwalian(self):
        print(f"{self.nama} mulai perwalian pada jam {time.ctime(time.time())}")
        time.sleep(2)
        print(f"{self.nama} selesai perwalian pada jam {time.ctime(time.time())}")
        # Thread menunggu di barrier
        barrier.wait()
        print(f"{self.nama} telah menyelesaikan perwaliannya\n")

# Data mahasiswa
mhs1 = Mahasiswa("Mahasiswa A", "001")
mhs2 = Mahasiswa("Mahasiswa B", "002")
mhs3 = Mahasiswa("Mahasiswa C", "003")

if __name__ == '__main__':
    # membuat thread baru untuk setiap mahasiswa
    t1 = threading.Thread(target=mhs1.perwalian)
    t2 = threading.Thread(target=mhs2.perwalian)
    t3 = threading.Thread(target=mhs3.perwalian)

    # menjalankan thread
    t1.start()
    t2.start()
    t3.start()

    # menunggu thread selesai
    t1.join()
    t2.join()
    t3.join()

    # menampilkan pesan ketika semua mahasiswa selesai perwalian
    print("Semua mahasiswa telah menyelesaikan perwaliannya pada jam: ", time.ctime(time.time()))

    start_time = time.time()
    end_time = time.time()
    print("Perbandingan data berjalan dan berhenti = ", end_time - start_time)

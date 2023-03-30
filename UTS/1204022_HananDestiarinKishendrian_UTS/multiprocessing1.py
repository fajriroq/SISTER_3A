import multiprocessing
import time

def sendok():
    # pekerjaan pertama
    print("Stok piring tersedia")
    time.sleep(2)
    print("Stok piring kososng")


def piring():
    # pekerjaan kedua
    print("Stok sendok tersedia")
    time.sleep(3)
    print("Stok sendrok kosong")


def pisau():
    # pekerjaan ketiga
    print("Stok pisau tersedia")
    time.sleep(1)
    print("Stok pisau kosong")


if __name__ == '__main__':
    # membuat proses baru untuk setiap pekerjaan
    p1 = multiprocessing.Process(target=sendok)
    p2 = multiprocessing.Process(target=piring)
    p3 = multiprocessing.Process(target=pisau)

    # menjalankan proses
    p1.start()
    p2.start()
    p3.start()

    # menunggu proses selesai
    p1.join()
    p2.join()
    p3.join()

    # menampilkan pesan ketika semua pekerjaan selesai
    print("Semua stok tersedia")

    # menampilkan pesan waktu pelunasan
    print("Waktu re-stok : ", time.ctime(time.time()))

    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    print("Perbandingan waktu stok kosong dan stok habis = ", end_time - start_time)
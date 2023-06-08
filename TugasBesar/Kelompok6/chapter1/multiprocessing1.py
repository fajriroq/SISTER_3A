import multiprocessing
import time


def tv():
    print("Tv tersedia")
    time.sleep(2)
    print("Tv terjual habis!!")


def radio():
    print("Radio tersedia")
    time.sleep(3)
    print("Radio terjual habis!!")


def laptop():
    print("Laptop tersedia")
    time.sleep(1)
    print("Laptop terjual habis!!")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=tv)
    p2 = multiprocessing.Process(target=radio)
    p3 = multiprocessing.Process(target=laptop)


    p1.start()
    p2.start()
    p3.start()


    p1.join()
    p2.join()
    p3.join()


    print("Semua barang habis terjual!!")


    print("Waktu re-stok : ", time.ctime(time.time()))

    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    print("Perbandingan waktu persediaan kosong dan tersedia = ", end_time - start_time)

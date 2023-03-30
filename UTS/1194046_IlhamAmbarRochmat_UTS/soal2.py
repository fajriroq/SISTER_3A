import multiprocessing
import time

def book_flight(name):
    print(f"{name} sedang memesan tiket pesawat...")
    time.sleep(2) # simulasi waktu pemesanan
    print(f"{name} berhasil memesan tiket pesawat!")

if __name__ == '__main__':
    # Daftar nama-nama penumpang yang ingin memesan tiket pesawat
    passenger_names = ['Alice', 'Bob', 'Charlie', 'David']

    # Membuat proses multiprocessing untuk setiap penumpang
    processes = []
    for name in passenger_names:
        p = multiprocessing.Process(target=book_flight, args=(name,))
        processes.append(p)
        p.start()

    # Menunggu hingga semua proses selesai
    for p in processes:
        p.join()

    print("Semua tiket pesawat telah dipesan!")

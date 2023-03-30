import multiprocessing
import time

def buy_crypto(name, amount):
    print(f"{name} melakukan pembelian crypto sejumlah {amount}...")
    time.sleep(2)
    print(f"{name} telah berhasil membeli crypto sejumlah {amount}.")

def sell_crypto(name, amount):
    print(f"{name} melakukan penjualan crypto sejumlah {amount}...")
    time.sleep(2)
    print(f"{name} telah berhasil menjual crypto sejumlah {amount}.")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=buy_crypto, args=('Alice', 5))
    p2 = multiprocessing.Process(target=sell_crypto, args=('Bob', 3))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Semua transaksi selesai.")

import multiprocessing
import random
import time

def buy_crypto(crypto_name, amount, price):
    # Simulasi proses pembelian crypto
    print(f"Proses pembelian {amount} {crypto_name} dengan harga {price} dimulai...")
    # Proses pembelian berlangsung selama 3 detik
    time.sleep(3)
    print(f"Proses pembelian {amount} {crypto_name} dengan harga {price} selesai.")
    print(f"Transaksi pembelian {amount} {crypto_name} senilai {amount*price} berhasil dilakukan.")

def sell_crypto(crypto_name, amount, price):
    # Simulasi proses penjualan crypto
    print(f"Proses penjualan {amount} {crypto_name} dengan harga {price} dimulai...")
    # Proses penjualan berlangsung selama 3 detik
    time.sleep(3)
    print(f"Proses penjualan {amount} {crypto_name} dengan harga {price} selesai.")
    print(f"Transaksi penjualan {amount} {crypto_name} senilai {amount*price} berhasil dilakukan.")

if __name__ == '__main__':
    # List crypto yang tersedia
    crypto_list = ['BTC', 'ETH', 'LTC', 'BCH', 'XRP']

    # Spawn child process untuk setiap transaksi crypto
    for i in range(10):
        # Pilih jenis transaksi secara acak
        transaksi = random.choice(['beli', 'jual'])

        # Pilih jenis crypto secara acak
        crypto_name = random.choice(crypto_list)

        # Pilih jumlah crypto secara acak
        amount = random.randint(1, 10)

        # Pilih harga crypto secara acak
        price = random.uniform(10000, 50000)

        # Buat child process untuk setiap transaksi
        if transaksi == 'beli':
            p = multiprocessing.Process(target=buy_crypto, args=(crypto_name, amount, price))
        else:
            p = multiprocessing.Process(target=sell_crypto, args=(crypto_name, amount, price))

        # Mulai child process
        p.start()

import multiprocessing
import time

# Fungsi untuk menghitung total pembayaran
def calculate_payment(payment_queue, total_payment):
    while True:
        # Ambil pembayaran dari queue
        payment = payment_queue.get()

        # Jika pembayaran adalah -1, artinya tidak ada pembayaran lagi
        if payment == -1:
            break

        # Tambahkan pembayaran ke total pembayaran
        total_payment.value += payment

# Fungsi untuk memproses pembayaran
def process_payment(payment_queue, amount):
    # Simulasi proses pembayaran
    time.sleep(1)
    print(f"Memproses pembayaran sejumlah {amount}")

    # Tambahkan pembayaran ke queue
    payment_queue.put(amount)

# Fungsi untuk menghitung total biaya sewa
def calculate_rental(rental_queue, total_rental):
    while True:
        # Ambil biaya sewa dari queue
        rental = rental_queue.get()

        # Jika biaya sewa adalah -1, artinya tidak ada biaya sewa lagi
        if rental == -1:
            break

        # Tambahkan biaya sewa ke total biaya sewa
        total_rental.value += rental

# Fungsi untuk menyewakan barang
def rent_item(rental_queue, item, price):
    # Simulasi proses penyewaan
    time.sleep(2)
    print(f"Barang {item} berhasil disewakan dengan harga {price}")

    # Tambahkan biaya sewa ke queue
    rental_queue.put(price)

# Fungsi untuk spawn child process
def spawn_process(target, args):
    p = multiprocessing.Process(target=target, args=args)
    p.start()
    return p

if __name__ == '__main__':
    # Inisialisasi queue dan shared variable
    payment_queue = multiprocessing.Queue()
    rental_queue = multiprocessing.Queue()
    total_payment = multiprocessing.Value('i', 0)
    total_rental = multiprocessing.Value('i', 0)

    # Buat parent process untuk menghitung total pembayaran dan biaya sewa
    payment_process = multiprocessing.Process(target=calculate_payment, args=(payment_queue, total_payment))
    rental_process = multiprocessing.Process(target=calculate_rental, args=(rental_queue, total_rental))
    payment_process.start()
    rental_process.start()

    # Spawning child process untuk menyewakan barang
    processes = [spawn_process(rent_item, (rental_queue, item, price)) for item, price in [("TV", 100), ("Kulkas", 200), ("AC", 300)]]

    # Tunggu sampai semua child process selesai
    for p in processes:
        p.join()

    # Tandai akhir pembayaran dan biaya sewa
    payment_queue.put(-1)
    rental_queue.put(-1)

    # Tunggu sampai parent process selesai menghitung total pembayaran dan biaya sewa
    payment_process.join()
    rental_process.join()

    # Print total pembayaran dan biaya sewa
    print(f"Total pembayaran: {total_payment.value}")
    print(f"Total biaya sewa: {total_rental.value}")

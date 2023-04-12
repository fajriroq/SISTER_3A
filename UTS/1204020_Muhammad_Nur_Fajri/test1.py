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

if __name__ == '__main__':
    # Inisialisasi queue dan shared variable
    payment_queue = multiprocessing.Queue()
    total_payment = multiprocessing.Value('i', 0)

    # Buat parent process untuk menghitung total pembayaran
    payment_process = multiprocessing.Process(target=calculate_payment, args=(payment_queue, total_payment))
    payment_process.start()

    # Spawning child process untuk memproses pembayaran
    processes = []
    for amount in [100, 200, 300]:
        p = multiprocessing.Process(target=process_payment, args=(payment_queue, amount))
        processes.append(p)
        p.start()

    # Tunggu sampai semua child process selesai
    for p in processes:
        p.join()

    # Tandai akhir pembayaran
    payment_queue.put(-1)

    # Tunggu sampai parent process selesai menghitung total pembayaran
    payment_process.join()

    # Cetak total pembayaran
    print(f"Total pembayaran: {total_payment.value}")

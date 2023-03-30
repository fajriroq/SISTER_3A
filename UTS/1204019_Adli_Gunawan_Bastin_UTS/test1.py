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
def process_payment(payment_queue, customer_name, car_type, rental_duration, rental_rate):
    # Simulasi proses pembayaran
    time.sleep(1)
    total_rental = rental_duration * rental_rate
    print(f"{customer_name} menyewa {car_type} selama {rental_duration} hari dengan harga {rental_rate} per hari")
    print(f"Total biaya sewa: {total_rental}")

    # Tambahkan pembayaran ke queue
    payment_queue.put(total_rental)

if __name__ == '__main__':
    # Inisialisasi queue dan shared variable
    payment_queue = multiprocessing.Queue()
    total_payment = multiprocessing.Value('i', 0)

    # Buat parent process untuk menghitung total pembayaran
    payment_process = multiprocessing.Process(target=calculate_payment, args=(payment_queue, total_payment))
    payment_process.start()

    # Spawning child process untuk memproses pembayaran
    processes = []
    for customer, car_type, duration, rate in [("Alice", "Sedan", 5, 150), ("Bob", "SUV", 3, 250), ("Charlie", "Minivan", 2, 200)]:
        p = multiprocessing.Process(target=process_payment, args=(payment_queue, customer, car_type, duration, rate))
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

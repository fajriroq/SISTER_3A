import multiprocessing
import time

# Fungsi untuk memproses pesanan


def process_order(order):
    print("Memproses pesanan:", order)
    # Simulasi waktu pengiriman
    time.sleep(2)
    print("Pesanan", order, "selesai diproses.")

# Fungsi untuk mengirim pesanan ke gudang


def send_order(order):
    print("Mengirim pesanan:", order)
    # Spawning process untuk memproses pesanan
    process = multiprocessing.Process(target=process_order, args=(order,))
    process.start()


if __name__ == '__main__':
    # Membuat beberapa process untuk mengirim pesanan
    send_order_process1 = multiprocessing.Process(
        target=send_order, args=("Order 1",))
    send_order_process2 = multiprocessing.Process(
        target=send_order, args=("Order 2",))
    send_order_process3 = multiprocessing.Process(
        target=send_order, args=("Order 3",))

    # Memulai process-process yang ada
    send_order_process1.start()
    send_order_process2.start()
    send_order_process3.start()

    # Menunggu process-process yang ada selesai
    send_order_process1.join()
    send_order_process2.join()
    send_order_process3.join()

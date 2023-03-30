import multiprocessing
import time

# Fungsi untuk memproses persediaan obat


def process_medicine_stock(medicine_name, quantity):
    print(f"Memproses persediaan obat {medicine_name}...")
    time.sleep(2)
    print(f"{quantity} {medicine_name} telah diproses")


if __name__ == '__main__':
    # Persediaan obat
    medicine_stock = {
        'Paracetamol': 100,
        'Amoxicillin': 50,
        'Omeprazole': 30,
        'Metformin': 75,
        'Simvastatin': 20
    }

    # Proses induk
    print(f"Persediaan obat sebelum diproses: {medicine_stock}")
    start_time = time.time()

    # Membuat proses baru untuk memproses setiap item pada persediaan obat
    processes = []
    for medicine, quantity in medicine_stock.items():
        process = multiprocessing.Process(
            target=process_medicine_stock, args=(medicine, quantity))
        processes.append(process)
        process.start()

    # Menunggu semua proses selesai
    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Waktu eksekusi: {end_time - start_time} detik")
    print(f"Persediaan obat setelah diproses: {medicine_stock}")

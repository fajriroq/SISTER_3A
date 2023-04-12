import multiprocessing
import time

def sort_palm_fruit(palm_fruit_id):
    # Simulasi proses penyortiran kelapa sawit
    time.sleep(1)
    
    print(f"Buah kelapa sawit dengan ID {palm_fruit_id} telah disortir")

if __name__ == '__main__':
    # Daftar kelapa sawit
    palm_fruit_list = [101, 102, 103, 104, 105]

    # Proses penyortiran kelapa sawit
    sort_processes = []
    for palm_fruit_id in palm_fruit_list:
        sort_process = multiprocessing.Process(target=sort_palm_fruit, args=(palm_fruit_id,))
        sort_processes.append(sort_process)
        sort_process.start()

    # Tunggu sampai semua proses selesai
    for sort_process in sort_processes:
        sort_process.join()

    # Tampilkan daftar kelapa sawit setelah penyortiran
    print(f"Daftar kelapa sawit setelah penyortiran: {palm_fruit_list}")

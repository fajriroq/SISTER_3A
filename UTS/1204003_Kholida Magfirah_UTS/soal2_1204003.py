import multiprocessing
import time

def register(participant):
    print(f"{participant['nama']} telah terdaftar")

def target_function(target_list):
    for target in target_list:
        register(target)

if __name__ == '__main__':

    print("\nPROSES PENGECEKAN !!\n")
   
    participants = [
        {"nama": "Fira", "umur": 23, "email": "fira@example.com"},
        {"nama": "Kholida", "umur": 15, "email": "kholida@example.com"},
        {"nama": "Magfirah", "umur": 30, "email": "magfirah@example.com"},
        {"nama": "Pira", "umur": 19, "email": "pira@example.com"},
        {"nama": "Piwa", "umur": 25, "email": "piwa@example.com"}
    ]

    processes = []
    start_time = time.time()
    

    num_workers = 3
    target_size = len(participants) // num_workers
    targets = [participants[i:i+target_size] for i in range(0, len(participants), target_size)]

    with multiprocessing.Pool(processes=num_workers) as pool:
        pool.map(target_function, targets)

    end_time = time.time()
 
    print(f"\nWaktu yang diperlukan untuk menyelesaikan proses: {end_time - start_time} detik\n")

import multiprocessing
import time

def sort_kelapa_sawit(id, kelapa_sawit):
   
    time.sleep(1)
    print(f"Kelapa sawit dengan ID {id} berhasil di-sort dengan kualitas {kelapa_sawit}.")

if __name__ == '__main__':

    kelapa_sawit_data = {
        1: 'bagus',
        2: 'kurang',
        3: 'baik',
        4: 'bagus',
        5: 'baik'
    }

   
    print("Proses sorting kelapa sawit dimulai...")


    processes = []
    for id, kualitas in kelapa_sawit_data.items():
        p = multiprocessing.Process(target=sort_kelapa_sawit, args=(id, kualitas))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


    print("Hasil sorting kelapa sawit:")
    for id, kualitas in kelapa_sawit_data.items():
        print(f"ID {id}: {kualitas}")

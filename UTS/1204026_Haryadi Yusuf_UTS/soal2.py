import multiprocessing
import time

jadwal_kuliah = [
    ["Sistem Tersebar", "Sitem Multimedia"],
    ["AI","Bahasa Inggris"],
    ["Statitistika", "Data Mining"]
]

def process_jadwal(kuliah):
    for i in range(len(kuliah)):
        time.sleep(1)  # simulasi pengolahan data
        print("Proses {} - Jadwal kuliah:".format(multiprocessing.current_process().name))
        print(kuliah[i])
        print()

if __name__ == '__main__':
    processes = []
    for i in range(len(jadwal_kuliah)):
        process = multiprocessing.Process(target=process_jadwal, args=(jadwal_kuliah[i],))
        processes.append(process)

    start_time = time.time()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Total waktu eksekusi: ", elapsed_time)

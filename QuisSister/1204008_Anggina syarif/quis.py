import random
import threading as tr
import time
import time as tm


jadwalMhs = [
    {'npm': 1204004, 'hari': 'senin', 'matkul': 'data mining'},
    {'npm': 1204025, 'hari': 'senin', 'matkul': 'sap 1'},
    {'npm': 1204011, 'hari': 'senin', 'matkul': 'sap 2'},
    {'npm': 12040204, 'hari': 'senin', 'matkul': 'ai'}
]

# add more data
for i in range(4):
    jadwalMhs.append({
        'npm': random.randint(1000000, 9999999),
        'hari': random.choice(['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']),
        'matkul': random.choice(['ai', 'data mining', 'gis', 'sistem pakar'])
    })

lock = tr.Lock()
barrier = tr.Barrier(len(jadwalMhs))


def job1():
    global jadwalMhs
    with lock:
        jadwal = jadwalMhs.pop()
    current = tr.current_thread()
    start = tm.time()
    print(f"Thread {current.name} started")
    print(f"Data Mahasiswa {jadwal['npm']} hari {jadwal['hari']} ada pelajaran {jadwal['matkul']}")
    time.sleep(random.randint(1,3))
    print(f"Thread {current.name} finished in {tm.time() - start} at {tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(tm.time()))}")
    barrier.wait()


def main():
    start = tm.time()
    print(f"Main thread start at {tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(start))}")

    threads: list[tr.Thread] = list()

    for i in range(len(jadwalMhs)):
        threads.append(tr.Thread(target=job1, name=f"Thread {i}"))

    threads.reverse()
    for i in threads:
        i.start()

    threads.reverse()
    for i in threads:
        i.join()

    print(f"Main Thread End in {tm.time() - start} at {tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(tm.time()))}")


if __name__ == '__main__':
    main()

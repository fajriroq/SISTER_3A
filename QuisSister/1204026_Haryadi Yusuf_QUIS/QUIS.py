import threading
import time
import queue

def Matkul(q, lock):
    curr = threading.current_thread()
    print(f"Thread {threading.current_thread().name} sedang berjalan")
    start = time.time()

    while True:
        subject = q.get()
        if subject is None:
            break
        lock.acquire()
        print(f"Mulai mata kuliah {subject}")
        lock.release()
        time.sleep(3)
        lock.acquire()
        print(f"Selesai mata kuliah {subject}")
        lock.release()
        print(f"Thread {threading.current_thread().name} selesai mengerjakan {subject} dalam waktu {time.time() - start}")

        q.task_done()

q = queue.Queue()

q.put("AI")
q.put("Sistem Tersebar")
q.put("Data Mining")
q.put("Statistika")

lock = threading.Lock()

threads = []
for i in range(4):
    t = threading.Thread(target=Matkul, args=(q, lock))
    t.start()
    threads.append(t)

q.join()

for i in range(4):
    q.put(None)

for t in threads:
    t.join()

print("Semua mata kuliah selesai")

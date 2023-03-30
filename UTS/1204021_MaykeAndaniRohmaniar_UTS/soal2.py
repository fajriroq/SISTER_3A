import multiprocessing
import time
import random

def clean_beach():
    print(f"[{time.ctime()}] Membersihkan Pantai...")
    time.sleep(random.randint(1,5))
    print(f"[{time.ctime()}] Membersihkan Pantai done!")

def plant_trees():
    print(f"[{time.ctime()}] Menanam Pohon...")
    time.sleep(random.randint(1,5))
    print(f"[{time.ctime()}] Menanam Pohon done!")

def feed_homeless():
    print(f"[{time.ctime()}] Memberi makan gelandangan...")
    time.sleep(random.randint(1,5))
    print(f"[{time.ctime()}] Memberi makan gelandangan done!")

if __name__ == '__main__':
    process_beach = multiprocessing.Process(target=clean_beach)
    process_trees = multiprocessing.Process(target=plant_trees)
    process_homeless = multiprocessing.Process(target=feed_homeless)


    process_beach.start()
    process_trees.start()
    process_homeless.start()


    process_beach.join()
    process_trees.join()
    process_homeless.join()

import threading 
import time
from queue import Queue

class InputNilai(threading.Thread):
    def __init__(self, name, nilai_queue):
        threading.Thread.__init__(self)
        self.name = name
        self.nilai_queue = nilai_queue

    def run(self):
        print(f"{self.name} memulai menginput nilai")
        for i in range(5):
            nilai = input(f"Masukkan nilai mahasiswa ke-{i+1}: ")
            self.nilai_queue.put(nilai)
            print(f"{self.name} : Nilai mahasiswa ke-{i+1} ({nilai}) telah dimasukkan ke dalam queue")
            time.sleep(5)
        self.nilai_queue.put(None)
        print(f"{self.name} telah selesai menginput nilai")
        
class HitungRataRata(threading.Thread):
    def __init__(self, name, nilai_queue):
        threading.Thread.__init__(self)
        self.name = name
        self.nilai_queue = nilai_queue

    def run(self):
        print(f"{self.name} memulai menghitung nilai rata-rata")
        total_nilai = 0
        jumlah_nilai = 0
        while True:
            nilai = self.nilai_queue.get()
            if nilai is None:
                self.nilai_queue.put(None)
                print(f"{self.name} telah selesai menghitung nilai rata-rata")
                break
            else:
                total_nilai += float(nilai)
                jumlah_nilai += 1
        rata_rata = total_nilai / jumlah_nilai
        print(f"Nilai rata-rata mahasiswa adalah {rata_rata:.2f}")

def main():
    nilai_queue = Queue()
    input_thread = InputNilai("Thread Input", nilai_queue)
    hitung_thread = HitungRataRata("Thread Hitung", nilai_queue)
    input_thread.start()
    hitung_thread.start()

    input_thread.join()
    hitung_thread.join()

    print("Program telah selesai")

if __name__ == "__main__":
    main()

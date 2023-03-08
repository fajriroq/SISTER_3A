import multiprocessing
import time

def foo():
    print ('Memulai Mengerjakan Tugas')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Mengerjakan Tugas  Selesai')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Proses sebelum Mengerjakan Tugas dijalankan:', p, p.is_alive())
    p.start()
    print ('Proses Mengerjakan Tugas berjalan:', p, p.is_alive())
    p.terminate()
    print ('Proses Mengerjakan Tugas dihentikan:', p, p.is_alive())
    p.join()
    print ('Proses joined:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)
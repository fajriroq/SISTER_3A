import multiprocessing
import time

def foo():
    print ('Memulai Fungsi')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Fungsi Selesai')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Proses sebelum dijalankan:', p, p.is_alive())
    p.start()
    print ('Proses berjalan:', p, p.is_alive())
    p.terminate()
    print ('Proses dihentikan:', p, p.is_alive())
    p.join()
    print ('Proses joined:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)

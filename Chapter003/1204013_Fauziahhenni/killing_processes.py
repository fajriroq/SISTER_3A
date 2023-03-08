import multiprocessing
import time

def foo():
    print ('Memulai Masak')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Masak  Selesai')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Proses sebelum masak dijalankan:', p, p.is_alive())
    p.start()
    print ('Proses memasak berjalan:', p, p.is_alive())
    p.terminate()
    print ('Proses memasak dihentikan:', p, p.is_alive())
    p.join()
    print ('Proses joined:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)
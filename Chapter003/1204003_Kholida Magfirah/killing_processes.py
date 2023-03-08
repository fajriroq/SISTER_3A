import multiprocessing
import time

def foo():
    print ('Memulai function')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Berakhir function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Process sebelum eksekusi:', p, p.is_alive())
    p.start()
    print ('Process berjalan:', p, p.is_alive())
    p.terminate()
    print ('Process terminated:', p, p.is_alive())
    p.join()
    print ('Process bergabung:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)

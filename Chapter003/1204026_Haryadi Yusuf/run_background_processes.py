import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("memulai %s \n" %name)
    if name == 'proses yang berjalan di latar belakang':
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("keluar dari %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='proses yang berjalan di latar belakang',\
                          target=foo)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='proses yang tidak berjalan di latar belakang',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    


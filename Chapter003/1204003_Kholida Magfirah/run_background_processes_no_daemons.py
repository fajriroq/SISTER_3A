import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Memulai %s \n" %name)
    if name == 'background_process':
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("Keluar %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='latar belakang proses',\
                          target=foo)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name='tanpa proses latar belakang',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    


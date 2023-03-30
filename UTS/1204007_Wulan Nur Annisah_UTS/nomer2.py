#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing
import time


def myFunc(i):
    print ('calling myFunc from process n°: %s' %i)
    for j in range (0,i):
        print('output from myFunc is :%s' %j)
    return

if __name__ == '__main__':
    for i in range(6 ):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()

class Berhasil(multiprocessing.Process):

    def run(self):
        print ('Pembayaran SPP %s' %self.name)
        return

if __name__ == '__main__':
    for i in range(6):
        process = Berhasil()
        process.start()
        process.join()

if __name__ == "__main__":
    start_time = time.time()
    size = 1000   
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("Semua Proses Berhasil")
    end_time = time.time()
    print("Selesai dalam waktu=", end_time - start_time)

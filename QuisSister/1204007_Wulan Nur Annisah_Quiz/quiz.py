import logging
import threading
import time
n_Threading=2
class buku(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.mensaje="Hola pembaca!!: "
    def menulis(self,msj):
        logging.debug('Menunggu kunci')
        self.lock.acquire()
        try:
            logging.debug('menulis buku')
            self.mensaje = self.mensaje+msj
        finally:
            self.lock.release()
    def Leer (self):
        print( self.mensaje)

def pembaca(lock,cond,buku):
    if barrier.n_waiting!=0:
        barrier.wait()
   
    with cond:
        cond.wait()
        logging.debug('Buku Ini Gratis')
        buku.Leer()


def penulis(lock,barrier,cond,buku):
    print(threading.current_thread().name,'Menunggu Penulis Lain')
    id_penulis=barrier.wait()
    logging.debug('Membaca buku')
    lock.acquire()
    with cond:
          logging.debug('Mengambil buku')
          Mensaje = str(threading.current_thread().name)
          buku.menulis(Mensaje)
          time.sleep(3)
          logging.debug('Buku Selesai ditulis')
          logging.debug('Buku ditaruh')
          lock.release()

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',

)

lock = threading.Lock()
NUM_THREADS = 2
buku=buku()
condition = threading.Condition()
barrier = threading.Barrier(NUM_THREADS)
h1 = threading.Thread(target=penulis,args=(lock,barrier,condition,buku), name='penulis 1',)
h1.start()

h3 = threading.Thread(target=pembaca,args=(lock,condition,buku), name='pembaca 1', )
h3.start()

h4 = threading.Thread(target=pembaca,args=(lock,condition,buku), name='pembaca 2',)
h4.start()

h2 = threading.Thread(target=penulis,args=(lock,barrier,condition,buku), name='penulis 2',)
h2.start()

h5 = threading.Thread(target=pembaca,args=(lock,condition,buku), name='pembaca 3', )
h5.start()

h6 = threading.Thread(target=pembaca,args=(lock,condition,buku), name='pembaca 4',)
h6.start()
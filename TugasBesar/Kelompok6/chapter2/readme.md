Import modul logging, threading, dan time.

Mengatur format pesan log menggunakan LOG_FORMAT. Pesan log akan mencakup timestamp (asctime), nama thread (threadName), level log (levelname), dan pesan itu sendiri (message). = LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'

Mengkonfigurasi logging dengan level logging.INFO dan format pesan log yang telah ditentukan. = logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

Membuat variabel items sebagai list kosong yang akan digunakan sebagai buffer untuk menyimpan produk. = items = []

Membuat objek condition menggunakan threading.Condition() untuk mengatur kondisi yang akan diawasi oleh thread. = condition = threading.Condition()

Membuat kelas pembeli1 yang merupakan turunan dari threading.Thread. = class pembeli1(threading.Thread):

Dalam kelas pembeli1, mendefinisikan metode pengunjung() yang akan dijalankan oleh thread. = def pengunjung(self):

Dalam metode pengunjung(), menggunakan blok with condition untuk memperoleh lock pada objek condition. = with condition:

Dalam blok with condition, melakukan pengecekan apakah buffer items kosong dengan len(items) == 0. Jika kosong, mencetak pesan log "PRODUK HABIS!!" dan menunggu dengan condition.wait(). = if len(items) == 0:
    logging.info('PRODUK HABIS!!')
    condition.wait()

Jika buffer items tidak kosong, mengeluarkan produk dengan items.pop() dan mencetak pesan log "Mendapat produk". = items.pop()
logging.info('Mendapat produk')

Mengirim sinyal bahwa buffer telah berubah dengan condition.notify(). = condition.notify()

Mendefinisikan metode run() yang akan berjalan ketika thread dijalankan. Dalam metode run(), melakukan iterasi sebanyak 10 kali dan memanggil metode pengunjung() setelah jeda waktu 2 detik menggunakan time.sleep(2). =

def run(self):
    for i in range(10):
        time.sleep(2)
        self.pengunjung()

Membuat kelas sales1 yang juga merupakan turunan dari threading.Thread.
class sales1(threading.Thread):
Dalam kelas sales1, mendefinisikan metode pengelola() yang akan dijalankan











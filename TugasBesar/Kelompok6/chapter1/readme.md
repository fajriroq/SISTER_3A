Import modul multiprocessing dan time.

Mendefinisikan tiga fungsi: tv(), radio(), dan laptop(). Setiap fungsi mencetak beberapa pesan ke layar menggunakan print(), menunggu selama beberapa detik menggunakan time.sleep(), dan mencetak pesan berikutnya setelah jeda waktu tertentu.
def tv():
    print("Tv tersedia")
    time.sleep(2)
    print("Tv terjual habis!!")

def radio():
    print("Radio tersedia")
    time.sleep(3)
    print("Radio terjual habis!!")

def laptop():
    print("Laptop tersedia")
    time.sleep(1)
    print("Laptop terjual habis!!")

Memeriksa apakah kode ini dijalankan sebagai program utama menggunakan if __name__ == '__main__':. Hal ini diperlukan dalam penggunaan modul multiprocessing untuk menghindari masalah saat menjalankan kode di lingkungan multiproses. = if __name__ == '__main__':


Membuat tiga objek Process menggunakan modul multiprocessing.Process(). Setiap objek Process menerima argumen target yang menunjukkan fungsi yang akan dijalankan oleh proses tersebut. = p1 = multiprocessing.Process(target=tv)
p2 = multiprocessing.Process(target=radio)
p3 = multiprocessing.Process(target=laptop)

Memulai setiap proses menggunakan metode start() untuk menjalankan fungsi-fungsi yang terkait. = p1.start()
p2.start()
p3.start()

Menggunakan metode join() untuk menunggu hingga setiap proses selesai. Dalam hal ini, join() digunakan setelah start() untuk memastikan bahwa semua proses selesai sebelum kode berikutnya dieksekusi. = p1.join()
p2.join()
p3.join()

Menghitung waktu yang diperlukan untuk menjalankan beberapa operasi menggunakan time.time(). Variabel start_time menyimpan waktu awal, dan setelah jeda 2 detik, variabel end_time menyimpan waktu akhir. Hasil perhitungan waktu di antara keduanya dicetak sebagai "Perbandingan waktu persediaan kosong dan tersedia".

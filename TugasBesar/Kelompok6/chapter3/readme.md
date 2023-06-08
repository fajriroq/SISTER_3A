Import modul multiprocessing, ctime dari modul time, dan random dari modul random. = import multiprocessing
from time import ctime, sleep
from random import random

Mendefinisikan fungsi function_square(data) yang akan mengembalikan hasil dari kuadrat data yang diberikan.=
def function_square(data):
    result = data * data
    return result

Mendefinisikan variabel barang1, barang2, dan barang3 yang masing-masing berisi nama barang 'Tv', 'Radio', dan 'Laptop'. =
barang1 = 'Tv'
barang2 = 'Radio'
barang3 = 'Laptop'

Memeriksa apakah kode ini dijalankan sebagai program utama menggunakan if __name__ == '__main__':. Hal ini diperlukan dalam penggunaan modul multiprocessing untuk menghindari masalah saat menjalankan kode di lingkungan multiproses.=
if __name__ == '__main__':

Membuat tiga list inputs1, inputs2, dan inputs3 yang berisi rentang angka tertentu. Setiap list ini akan digunakan sebagai input untuk pemrosesan paralel. = 
inputs1 = list(range(8, 9))
inputs2 = list(range(10, 11))
inputs3 = list(range(20, 21))

Membuat multiprocessing pool dengan multiprocessing.Pool(processes=4) yang menggunakan 4 proses. = 
pool = multiprocessing.Pool(processes=4)
Menggunakan pool.map() untuk melakukan pemrosesan paralel pada setiap list input dengan fungsi function_square(). 

Hasilnya akan disimpan dalam pool_outputs1, pool_outputs2, dan pool_outputs3. = 
pool_outputs1 = pool.map(function_square, inputs1)
pool_outputs2 = pool.map(function_square, inputs2)
pool_outputs3 = pool.map(function_square, inputs3)

Mengatur variabel terjual1, terjual2, dan terjual3 untuk masing-masing barang yang terjual. = 
terjual1 = barang1
terjual2 = barang2
terjual3 = barang3

Menghasilkan nilai acak (value) antara 0 dan 5 menggunakan random() dan melakukan jeda waktu sesuai dengan nilai tersebut menggunakan sleep(value). =
value = random() * 5
sleep(value)

Mencetak informasi barang yang terjual beserta nomor barang, waktu, dan tanggal menggunakan print(). Nilai value digunakan untuk waktu, pool_outputs1, pool_outputs2, dan pool_outputs3 digunakan untuk nomor barang yang terjual, dan ctime() digunakan untuk mencetak tanggal saat ini. = print(f'Barang Terjual: \nNama Barang: %s \nNomor Barang: %s \nWaktu : {value} \nTanggal: %s \



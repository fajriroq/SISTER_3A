STUDI KASUS : PROGRAM PENGELOLAAN INVENTORY BARANG

Pada file inventory_server.py
![image](https://github.com/kholidamagfirah/1204003_Maps/assets/74235340/9fa40543-1ba3-4127-a36a-80e2972dbf17)

![image](https://github.com/kholidamagfirah/1204003_Maps/assets/74235340/c59422e0-e5e7-4d8c-b3c8-942000285536)

Inventory adalah kelas yang mewakili inventaris barang. Dalam kelas ini, terdapat metode untuk menambahkan, menghapus, mengubah, dan mendapatkan informasi barang.
do_something() adalah fungsi yang hanya mencetak "Doing something". Fungsi ini digunakan untuk demonstrasi.
barrier() adalah fungsi yang menggunakan MPI untuk menunggu semua proses mencapai titik sinkronisasi sebelum melanjutkan. Fungsi ini digunakan untuk demonstrasi.
myFunc() adalah fungsi yang hanya mencetak "Running myFunc". Fungsi ini digunakan untuk demonstrasi.
serve_inventory() adalah fungsi yang menjalankan server Pyro4 untuk melayani permintaan dari client. Server ini akan memanggil metode-metode yang sesuai di dalam objek Inventory untuk menangani operasi pada inventaris barang.
Fungsi main() adalah fungsi utama program. Pada proses dengan rank 0 (rank server), server Pyro4 akan dijalankan dengan menggunakan await serve_inventory(). Pada proses dengan rank selain 0 (rank client), fungsi do_something() akan dijalankan, kemudian fungsi barrier() akan digunakan untuk sinkronisasi antar proses, dan terakhir myFunc() akan dijalankan menggunakan await untuk menjalankan fungsi sebagai asyncio coroutine.

Pada file inventory_client.py
![image](https://github.com/kholidamagfirah/1204003_Maps/assets/74235340/3acbbdc4-dc88-4da8-826c-296d9e860821)

Fungsi connect_to_server() adalah fungsi yang menghubungkan client ke server Pyro4 dan menampilkan menu inventaris barang kepada pengguna. Pengguna dapat memilih opsi yang sesuai untuk menambah, menghapus, mengubah, atau mendapatkan informasi barang.
Fungsi main() adalah fungsi utama program. Pada asyncio event loop, connect_to_server() akan dijalankan menggunakan await untuk menjalankan fungsi sebagai asyncio coroutine.
Disini saya membuat program yang menggunakan teknik lock dan barrier untuk menghindari masalah race condition dan memastikan bahwa semua thread telah selesai sebelum program berakhir. Program ini menggunakan studi kasus jadwal kuliah.

Pada awal program, dibuat sebuah list bernama jadwalMhs yang berisi jadwal mahasiswa dalam bentuk dictionary. Kemudian, menggunakan loop for, program menambahkan data jadwal mahasiswa secara acak ke dalam list.

Program juga mendefinisikan sebuah thread lock dan barrier. Thread lock digunakan untuk memastikan bahwa hanya satu thread yang dapat mengakses data jadwal mahasiswa pada satu waktu. Sedangkan thread barrier digunakan untuk menunda eksekusi semua thread sampai semua thread selesai.

Selanjutnya, program mendefinisikan sebuah fungsi bernama job1 yang akan dieksekusi oleh setiap thread. Fungsi ini menggunakan lock untuk mengambil satu item dari list jadwalMhs, mencetak jadwal mahasiswa yang diambil, dan kemudian menunggu selama waktu yang acak antara 1 hingga 3 detik sebelum mencetak bahwa thread selesai dan menyelesaikan tugas. Job1 juga menggunakan barrier dan lock untuk melakukan sinkronisasi antar thread.

Program selanjutnya mendefinisikan fungsi main, yang merupakan fungsi utama program. Fungsi ini mencetak pesan bahwa thread utama telah dimulai, membuat objek thread sebanyak jumlah item dalam list jadwalMhs, dan membalikkan urutan thread agar thread terakhir yang dibuat dieksekusi terlebih dahulu.

Program kemudian memulai setiap thread, menunggu setiap thread selesai, dan kemudian mencetak pesan bahwa thread utama telah selesai dan waktu total eksekusi.
![Gambar Screenshoot](1204004_gambar.png)
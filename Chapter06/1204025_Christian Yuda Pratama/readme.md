## TUGAS 1 
Projek ini bertujuan untuk mengilustrasikan penggunaan Celery dalam menjalankan tugas secara asinkron dalam aplikasi Python. Dalam proyek ini, saya menggunakan Celery untuk menjalankan tugas sederhana berupa penjumlahan dua angka. Tujuan dari proyek ini adalah memperlihatkan bagaimana tugas tersebut dapat dikirim ke antrian Celery dan dijalankan secara terpisah oleh worker Celery, tanpa menghambat jalannya aplikasi utama.

Dengan menggabungkan Celery dengan RabbitMQ sebagai broker pesan, proyek ini memperlihatkan cara mengatur sistem antrian tugas yang efisien. Celery memungkinkan saya untuk mengirim tugas ke worker yang tersedia secara asynchronous, sehingga saya dapat melanjutkan eksekusi aplikasi utama tanpa harus menunggu tugas selesai.

Melalui proyek ini, Anda dapat mempelajari bagaimana mengkonfigurasi Celery, mengirim tugas ke antrian menggunakan Celery, menjalankan worker Celery untuk mengeksekusi tugas, serta mengakses hasil tugas yang telah selesai dieksekusi.
[ini gambar celery](celery.PNG)

## Tugas 2

Proyek ini adalah contoh sederhana tentang bagaimana komunikasi jarak jauh dapat dilakukan menggunakan Pyro4. 
Dalam proyek ini, terdapat dua program: server dan klien. Server berfungsi untuk menerima pesan dari klien dan menyimpannya. Sedangkan klien berfungsi untuk mengirimkan pesan ke server dan juga dapat melihat pesan-pesan sebelumnya yang telah dikirim.

Ketika server dijalankan, ia akan membuka koneksi dan menunggu pesan dari klien. Saat klien dijalankan, ia akan terhubung ke server dan memungkinkan pengguna untuk memasukkan pesan. Setelah pesan dikirim, server akan menerimanya dan mencetaknya. Klien juga dapat meminta daftar pesan yang telah dikirim sebelumnya dari server.

Proyek ini menggambarkan bagaimana Pyro4 dapat digunakan untuk menghubungkan komputer yang berbeda melalui jaringan dan memungkinkan komunikasi antara server dan klien. 
[ini gambar pyro4](pyro4.PNG)

## Tugas 3

Project di atas adalah contoh implementasi sederhana dari komunikasi client-server menggunakan socket di Python. Terdapat dua skrip: server.py sebagai server dan client.py sebagai client.

Server menerima koneksi dari client dan menerima pesan dari client. Setelah itu, server mengubah pesan menjadi huruf kapital dan mengirimkan responsnya kembali ke client. Server terus menerima koneksi dari client lain dan melakukan proses yang sama.

Client menghubungkan dirinya ke server dan meminta pengguna memasukkan pesan. Pesan tersebut dikirim ke server, dan client menerima respons dari server. Respons tersebut kemudian ditampilkan ke pengguna.
[ini gambar socket](socket.PNG)


LINK VIDEO YOUTUBE = [TUGAS CHAPTER 6](https://youtu.be/olVWth-L3po)
https://youtu.be/olVWth-L3po

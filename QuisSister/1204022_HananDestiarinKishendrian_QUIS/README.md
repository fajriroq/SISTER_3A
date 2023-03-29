Pada quiz ini saya membuat studi kasus tentang tagihan dengan menggunakan threading menggunakan objek barrier.

Pada code tersebut membuat sebuah kelas Tagihan dengan atribut nama dan jenis. setiap tagihan memiliki method tagihan_1() yang nanti nya akan menampilkan pesan tentang tagihan dengan waktu tunggu selama 2 detik. lalu thread menunggu pada barrier terlebihdahulu sebelum menampilkan pesan bahwa pembayaran tagihan telah lunas.

lalu pada code tersebut terdapat 3 objek tagihan yaitu tagihan air, listrik, dan WIFI, setiap objek tagihan dimasukan kedalam thread baru yaitu t1, t2, t3 lalu di jalankan dengan menggunakan method start(). lalu program menunggu hingga semua thread selesai dijalankan menggunakan method join().

setelah semua thread telah selesai di jalankan, maka program akan menampilkan pesan tenggang waktu pelunasan dengan menggunakan method ctime() dari modul time. lalu program menunggu selama 2 detik menggunakan method sleep() sebelum menampilkan perbandingan waktu tagihan dan pelunasan menggunakan method time()

hasil seperti pada gambar di bawah ini
![](Screenshot (1040).png)

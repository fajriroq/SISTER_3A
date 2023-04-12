**SOAL 1 :**

Pada File soal1_1204003  program akan meminta input data peserta berupa nama, umur, dan alamat menggunakan fungsi input. Selanjutnya, process akan di-spawn menggunakan multiprocessing.Process dengan target register_participant dan argumen (nama, umur, alamat, lomba, email) yang sudah dimasukkan sebelumnya.
Setelah itu, process akan dijalankan dengan memanggil method start() dan menunggu proses selesai dengan method join(). Terakhir, setelah proses selesai, akan ditampilkan pesan "Proses pendaftaran selesai".

![Screenshot (272)](https://user-images.githubusercontent.com/74235340/228793917-9556c7b5-9fd2-4f17-b074-c151204e3f4a.png)

**SOAL 2 :**

Penjelasan pada file soal2_1204003:

Pertama-tama, kita mengimpor modul multiprocessing dan time.
Selanjutnya, kita mendefinisikan sebuah fungsi register yang akan dipanggil untuk mendaftarkan peserta lomba.
Kemudian, kita mendefinisikan sebuah fungsi target_function yang akan digunakan untuk menjalankan fungsi register pada setiap target.
Selanjutnya, kita membuat sebuah list berisi daftar peserta lomba.
Setelah itu, kita menghitung waktu awal program dijalankan menggunakan fungsi time.time().
Kita membagi list peserta menjadi beberapa target dengan ukuran yang sama untuk setiap worker dengan menggunakan variabel num_workers dan target_size.
Kemudian, kita membuat sebuah pool dengan jumlah worker sebanyak num_workers menggunakan perintah multiprocessing.Pool(processes=num_workers).
Terakhir, kita menjalankan fungsi target_function untuk setiap target secara bersamaan menggunakan perintah pool.map(target_function, targets).
Setelah semua worker selesai, kita menghitung waktu akhir program dijalankan menggunakan fungsi time.time() dan mencetak waktu yang diperlukan untuk menjalankan program.
Dengan menggunakan fungsi targeting, kita dapat membagi pekerjaan mendaftarkan peserta lomba menjadi beberapa target dengan ukuran yang sama untuk setiap worker sehingga waktu yang diperlukan untuk mendaftarkan seluruh peserta dapat lebih cepat dibandingkan dengan menjalankan fungsi register secara serial.

![Screenshot (273)](https://user-images.githubusercontent.com/74235340/228794967-fef59777-2d3f-45b6-b5a9-9e8295980ae6.png)

**SOAL 3 :**

Pada file soal3_1204003, program akan meminta input data peserta berupa nama, umur, dan alamat pada rank 0 menggunakan fungsi input. Selanjutnya, data tersebut akan dikirimkan ke rank 1 menggunakan point-to-point communication (PTPC) dengan menggunakan fungsi comm.send.

Di rank 1, data tersebut akan diterima menggunakan fungsi comm.recv.

Selanjutnya, nilai age akan dibroadcast ke semua process menggunakan collective communication comm.bcast.

Program juga membuat topologi 2D dengan ukuran 2x2 dan melakukan reduksi nilai age dari semua process ke rank 0 menggunakan collective communication cart_comm.Reduce.

Terakhir, pada rank 0, nilai age yang sudah direduksi akan ditampilkan pada pesan "Proses pendaftaran selesai".

Dalam contoh ini, PTPC digunakan untuk mengirimkan data antar process, collective communication digunakan untuk melakukan operasi pada data yang sama pada semua process, dan topologies digunakan untuk membuat topologi 2D yang dapat digunakan untuk melakukan operasi pada subset dari process.

![Screenshot (274)](https://user-images.githubusercontent.com/74235340/228795779-fbb0453d-f5b1-4093-85a3-b2e485d97088.png)



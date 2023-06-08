Skrip TB di atas menggambarkan pengelolaan gaji karyawan menggunakan multiprocessing, condition, dan asyncio. Berikut adalah penjelasan singkatnya:

1. Terdapat dua fungsi utama: `hitung_gaji()` dan `pengelola_gaji()`.
   - `hitung_gaji()` digunakan untuk menghitung gaji setiap karyawan. Setiap karyawan akan menunggu persetujuan dari pengelola sebelum menerima gaji.
   - `pengelola_gaji()` bertindak sebagai pengelola yang mengeluarkan gaji dan memberi tahu karyawan-karyawan yang sedang menunggu persetujuan.

2. Dalam blok `if __name__ == '__main__':`, objek `Condition` dibuat untuk mengatur kondisi dan sinkronisasi antara karyawan dan pengelola.

3. Daftar karyawan diinisialisasi dengan nama-nama karyawan.

4. Proses karyawan dibuat menggunakan multiprocessing. Setiap proses menghitung gaji untuk satu karyawan dengan memanggil fungsi `hitung_gaji()`. Mereka juga menerima objek `Condition` sebagai argumen.

5. `asyncio.sleep(2)` digunakan untuk memberikan jeda selama 2 detik sebelum pengelola mengeluarkan gaji. Ini memberi kesempatan bagi semua proses karyawan untuk memulai dan menunggu persetujuan.

6. Proses pengelola dibuat menggunakan multiprocessing. Proses ini memanggil fungsi `pengelola_gaji()` dan juga menerima objek `Condition` sebagai argumen.

7. Proses utama (main process) menunggu semua proses karyawan selesai menggunakan `p.join()`.

8. Setelah proses karyawan selesai, proses utama memberi tahu pengelola bahwa semua proses telah selesai dengan memanggil `condition.notify()`.

9. Proses utama kemudian menunggu proses pengelola selesai menggunakan `pengelola.join()`.

10. Setelah semua proses selesai, pesan "Semua proses selesai" dicetak.

Skrip tersebut memanfaatkan multiprocessing untuk menjalankan beberapa proses secara bersamaan, condition untuk mengatur sinkronisasi antara proses, dan asyncio untuk memberikan jeda sebelum pengelola mengeluarkan gaji.


Skrip MPI atas adalah contoh penggunaan MPI (Message Passing Interface) dengan menggunakan modul `mpi4py` untuk melakukan penghitungan gaji karyawan secara terdistribusi. Berikut adalah penjelasan singkatnya:

1. Modul `mpi4py` diimpor dari package `MPI`.

2. Daftar karyawan yang akan diproses disimpan dalam variabel `karyawan`.

3. MPI diinisialisasi dengan memanggil `MPI.COMM_WORLD` dan mendapatkan rank (nomor identifikasi proses) dan size (jumlah total proses).

4. Variabel `karyawan_per_process` menentukan jumlah karyawan yang akan diproses oleh setiap proses. Ini dihitung dengan membagi jumlah karyawan dengan ukuran total proses.

5. Fungsi `hitung_gaji()` digunakan untuk menghitung gaji karyawan berdasarkan posisi mereka. Karyawan dengan posisi "Staff" akan mendapatkan gaji 10% lebih tinggi, posisi "Manager" akan mendapatkan gaji 20% lebih tinggi, dan posisi "Supervisor" akan mendapatkan gaji 30% lebih tinggi.

6. Pada proses master (rank 0), variabel `total_gaji` diinisialisasi dengan nilai 0. Kemudian, loop dilakukan untuk menghitung gaji karyawan pada proses master. Setelah itu, loop dilakukan untuk menerima total gaji dari proses lain menggunakan `comm.recv()`. Total gaji dari semua proses ditambahkan ke `total_gaji` dan dicetak.

7. Pada proses-proses lain (dengan rank selain 0), variabel `total_gaji` diinisialisasi dengan nilai 0. Loop dilakukan untuk menghitung gaji karyawan pada proses tersebut. Setelah itu, total gaji dikirim ke proses master menggunakan `comm.send()`.

Skrip ini memanfaatkan MPI untuk membagi pekerjaan penghitungan gaji karyawan ke beberapa proses yang berjalan secara paralel. Setiap proses menghitung gaji untuk karyawan yang ditugaskan ke mereka, dan proses master mengumpulkan hasilnya untuk mendapatkan total gaji dari semua karyawan.
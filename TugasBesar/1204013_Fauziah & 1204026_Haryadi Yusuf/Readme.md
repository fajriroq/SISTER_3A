Implementasi pemesanan tiket konser

[1](1.png)![1](https://github.com/fauziahhennihasibuann/SISTER_3A/assets/114493159/b47a0c0d-0211-47a5-a377-52d53169ca4c)

Program di atas menggunakan modul multiprocessing untuk melakukan pemesanan tiket konser secara paralel. Terdapat fungsi book_concert_ticket yang digunakan untuk melakukan pemesanan tiket. Program ini menggunakan beberapa informasi konser yang disimpan dalam kamus (dictionary). Setiap konser dijalankan sebagai proses terpisah menggunakan objek Process dari modul multiprocessing. Setelah semua proses selesai, program mencetak pesan bahwa pemesanan tiket konser telah selesai. Dengan menggunakan multiprocessing, program ini dapat melakukan pemesanan tiket secara efisien dengan memanfaatkan pemrosesan paralel.



[2](./2.png)![2](https://github.com/fauziahhennihasibuann/SISTER_3A/assets/114493159/563a5c2c-cc7c-442a-8b5c-fd1d45252c6c)

Program di atas menggunakan modul threading untuk melakukan pemesanan tiket konser secara paralel menggunakan thread. Program ini memiliki fungsi book_ticket yang digunakan untuk memesan tiket konser. Terdapat juga daftar konser yang tersedia. Pemesanan tiket dilakukan oleh beberapa thread secara bersamaan, dan menggunakan objek barrier untuk melakukan sinkronisasi antara thread. Setelah semua thread selesai, program mencetak pesan bahwa pemesanan tiket telah selesai. Dengan menggunakan threading, program ini dapat melakukan pemesanan tiket secara efisien dengan memanfaatkan pemrosesan paralel.




[3](3.png)![3](https://github.com/fauziahhennihasibuann/SISTER_3A/assets/114493159/933574c0-db34-49a7-9f17-5eb1356071cb)

Program di atas menggunakan modul multiprocessing untuk melakukan pemesanan tiket konser secara paralel menggunakan process. Setiap konser dijadwalkan untuk diproses secara independen. Program mengukur waktu eksekusi total dari awal hingga akhir. Dengan menggunakan multiprocessing, program ini dapat melakukan pemesanan tiket secara efisien dengan memanfaatkan pemrosesan paralel menggunakan process.




[4](4.png)![4](https://github.com/fauziahhennihasibuann/SISTER_3A/assets/114493159/aaf6c2c7-9a68-410f-93d2-b326d3452446)

Program di atas menggunakan modul mpi4py untuk melakukan pemesanan tiket konser secara paralel menggunakan MPI (Message Passing Interface). Program ini menggunakan komunikator MPI untuk mengkoordinasikan proses-proses yang berjalan. Setiap proses memiliki tugas untuk mencetak informasi pemesanan tiket konser. Proses dengan peringkat 0 mengirimkan data konser kepada proses-proses lain, sementara proses-proses lain menerima data konser tersebut dan melakukan pencetakan. Dengan menggunakan MPI, program ini dapat melakukan pemesanan tiket konser secara efisien dengan memanfaatkan pemrosesan paralel dan komunikasi antar proses.




[5](5.png)![5](https://github.com/fauziahhennihasibuann/SISTER_3A/assets/114493159/37646d9e-1fc3-4f2a-9fa1-e543df5ca7b5)

Program di atas menggunakan modul asyncio untuk melakukan pemesanan tiket konser secara paralel menggunakan async/await. Setiap konser dievaluasi sebagai coroutine yang memanggil fungsi book_ticket untuk melakukan pemesanan tiket secara simulasi. Program menggunakan asyncio.create_task untuk membuat tugas (task) asinkron untuk setiap konser dan asyncio.gather untuk menunggu semua tugas selesai dieksekusi. Dengan menggunakan asyncio, program ini dapat melakukan pemesanan tiket konser secara efisien dengan memanfaatkan pemrograman asinkron dan event loop yang dioptimalkan oleh asyncio.




[6](6.png)![6](https://github.com/fauziahhennihasibuann/SISTER_3A/assets/114493159/25a7aa6a-c4fc-4db8-8d79-b1e083444de3)

Program di atas menggunakan modul `Pyro4` untuk membuat server aplikasi pemesanan tiket konser menggunakan Remote Procedure Call (RPC). Server ini memiliki kelas `TicketBooking` yang terdaftar sebagai objek Pyro4 dan memiliki metode `book_ticket` untuk melaksanakan logika pemesanan tiket. Server menjalankan _daemon_ Pyro4 untuk menerima panggilan jarak jauh dan menghubungkan objek `TicketBooking` ke URI. Klien dapat menggunakan URI tersebut untuk terhubung ke server dan memanggil metode `book_ticket` untuk memesan tiket konser. Dengan menggunakan `Pyro4`, program ini memungkinkan komunikasi jarak jauh antara klien dan server melalui RPC untuk melakukan pemesanan tiket konser.

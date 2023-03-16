
Program ini menginisialisasi sebuah antrian yang berisi nama-nama mata kuliah. Kemudian, beberapa thread dibuat untuk memproses antrian tersebut secara paralel. Setiap thread akan mengambil mata kuliah dari antrian dan memprosesnya. Sebuah lock digunakan untuk mengatur akses ke bagian kode yang sama oleh beberapa thread sekaligus agar tidak terjadi race condition. Setelah semua thread selesai memproses antrian, program menunggu thread untuk keluar dan mencetak pesan bahwa semua mata kuliah telah selesai diproses.

Hasil Screenshoot program
![Gambar Screenshoot](1204026_gambar.png)
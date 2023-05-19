Link Youtube https://youtu.be/LP560d8m-44
Pyro4

Python Remote Object bekerja seperti RMI (Remote Method Invocation) yang memungkinkan
untuk memanggil method object jarak jauh dengan proses berbeda.

Chain Topology 

untuk menerapkan chain topology pada Pyro4 maka harus menerapkan chain objek dan Client Server Objek
Dimana class chain mengalihkan panggilan ke server berikutnya dengan memproses pesan input dan alamat server yang menjadi tujuan.

Server Chain 1

Server 1 memulai proses dan menyimpan pesan kepada server 2 untuk objek 2
![WhatsApp Image 2023-05-16 at 19 47 49](https://github.com/Wulannur/lagi/assets/74166336/a04bed91-ec7a-487a-8e3e-b9f9b9e154aa)

Server 2 memulai proses dan menyimpan pesan kepada server 3 untuk objek 2
![WhatsApp Image 2023-05-16 at 19 49 10](https://github.com/Wulannur/lagi/assets/74166336/e6efe944-a4c9-488b-a072-c7f9ebaa651a)

Server 3 memulai proses dan menyimpan pesan kepada server 1 untuk objek 2
![WhatsApp Image 2023-05-16 at 19 49 39](https://github.com/Wulannur/lagi/assets/74166336/75f2fdfe-a091-4a7c-80cf-1e8e88178d02)

Maka server akan kembali pada titik awal.
![WhatsApp Image 2023-05-16 at 19 50 11](https://github.com/Wulannur/lagi/assets/74166336/7157ed9e-53ed-4962-8f90-a34dd7006953)

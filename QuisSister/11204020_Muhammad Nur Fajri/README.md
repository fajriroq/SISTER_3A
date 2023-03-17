# Soal Quis Sistem Tersebar


Baris 7-12: Class ProgramInput diperbaharui dengan menerima parameter tambahan, yaitu objek barrier. Objek barrier akan digunakan untuk sinkronisasi antar thread sehingga semua thread selesai menjalankan task-nya sebelum program berakhir. Baris 23-28: Setelah thread selesai memasukkan nilai, thread akan menunggu di barrier hingga semua thread selesai memasukkan nilai sebelum mencetak hasilnya. Baris 33-38: Fungsi main() diperbaharui dengan membuat objek barrier dan mengirimkannya sebagai parameter ke setiap thread. Setelah semua thread dimulai, fungsi main() akan menunggu di barrier hingga semua thread selesai menjalankan task-nya. Setelah semua thread selesai, waktu yang diperlukan program untuk selesai dihitung dan dicetak. Baris 38 : melakukan sinkronasi waktu dari memulai program execute hingga program selesai di execute

picture 1
![image](https://user-images.githubusercontent.com/86406309/225889003-bcf63927-647b-4fab-8db7-a2984ddf7dcc.png)



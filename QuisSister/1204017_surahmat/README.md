## penjelasan studi kasus: Nilai

sinopsis: pada program ini menerapkan penginputan nilai  pada mahasiswa, ketika user ingin menilai terdapat sbeuah pid dan waktu program yang berjalan dan kapan 
          selesai waktu program berjalan tersbut.



Baris 7-12: Class ProgramInput diperbaharui dengan menerima parameter tambahan, yaitu objek barrier. Objek barrier akan digunakan untuk sinkronisasi antar thread sehingga semua thread selesai menjalankan task-nya sebelum program berakhir.
Baris 23-28: Setelah thread selesai memasukkan nilai, thread akan menunggu di barrier hingga semua thread selesai memasukkan nilai sebelum mencetak hasilnya.
Baris 33-38: Fungsi main() diperbaharui dengan membuat objek barrier dan mengirimkannya sebagai parameter ke setiap thread. Setelah semua thread dimulai, fungsi main() akan menunggu di barrier hingga semua thread selesai menjalankan task-nya. Setelah semua thread selesai, waktu yang diperlukan program untuk selesai dihitung dan dicetak.
Baris 38 : melakukan sinkronasi  waktu dari memulai program execute hingga program selesai di execute

## picture execute 1
![image](https://user-images.githubusercontent.com/90734813/225613353-5ef31711-c4c1-43a0-9ea3-3c4a753f9729.png)

## picture execute 2
![image](https://user-images.githubusercontent.com/90734813/225613555-9bb27514-c179-44f8-b0c4-3ade37327e42.png)


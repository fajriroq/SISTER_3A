** Pada Chapter ini akan membahas :**
1. Memperkenalkan komputasi terdistribusi
2. Menggunakan modul soket Python
3. Manajemen tugas terdistribusi dengan Celery
4. Pemanggilan Metode Jarak Jauh (RMI) dengan Pyro4

## 1. Socket ##
Soket adalah objek perangkat lunak yang memungkinkan data dikirim dan diterima antara host jarak jauh (melalui jaringan) atau antara proses lokal, seperti Inter-Process Communication (IPC).
Kesuksesan dan penyebaran teknologi soket berjalan seiring dengan perkembangan internet. Faktanya, kombinasi soket dengan internet telah membuat komunikasi antar mesin jenis apa pun, dan/atau tersebar di seluruh dunia, menjadi sangat mudah (setidaknya jika dibandingkan dengan sistem lain).
Output Socket :


## 2. Celery ##
Celery adalah kerangka kerja Python yang mengelola tugas terdistribusi dengan mengikuti pendekatan middleware berorientasi objek. Fitur utamanya adalah penanganan banyak tugas kecil dan mendistribusikannya ke banyak node komputasi. Akhirnya, hasil setiap tugas akan diolah kembali untuk menyusun solusi keseluruhan.
Output Celery :


## 3. Pyro4 ##
Pyro singkatan dari Python Remote Objects. Ini bekerja persis seperti Java RMI (Remote Method Invocation) yang memungkinkan untuk memanggil metode dari objek remote (yang terletak dalam proses yang berbeda) persis seolah-olah objek tersebut adalah lokal (milik proses yang sama di mana pemanggilan berjalan).
Output Pyro4 :
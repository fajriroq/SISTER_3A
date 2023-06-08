server 
Import modul Pyro4.

Mendefinisikan kelas Server yang akan menjadi objek server remote. Metode welcomeMessage diberi decorator @Pyro4.expose agar dapat diakses secara remote. Metode ini menerima argumen name dan mengembalikan pesan "Barang Yang Akan Dibeli" disertai dengan nilai name yang dikonversi menjadi string. = 

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return "Barang Yang Akan Dibeli " + str(name)
    
Mendefinisikan fungsi startServer() untuk memulai server. Langkah-langkahnya sebagai berikut:

Membuat objek Server.
Membuat objek daemon Pyro4 menggunakan Pyro4.Daemon().
Mencari nameserver Pyro4 dengan Pyro4.locateNS().
Mendaftarkan objek server ke nameserver dengan menggunakan daemon.register(server).
Mencetak URI (Uniform Resource Identifier) objek yang di-register.
Memulai loop permintaan daemon dengan daemon.requestLoop() untuk melayani panggilan remote.

Memeriksa apakah kode ini dijalankan sebagai program utama menggunakan if __name__ == "__main__":. Hal ini diperlukan dalam penggunaan modul Pyro4.

client
Import modul Pyro4.

Menggunakan input dari pengguna untuk mendapatkan nama barang elektronik yang ingin dibeli. = 
name = input("Barang Elektronik Apa Yang Mau Anda Beli ? ").strip()

Membuat objek proxy server dengan menggunakan URI PYRONAME:server. URI ini digunakan untuk mencari objek server yang telah didaftarkan dengan nama "server" pada nameserver Pyro4. =
server = Pyro4.Proxy("PYRONAME:server")
Memanggil metode welcomeMessage(name) pada objek server dan mencetak hasilnya.


import Pyro4

def main():
    ns = Pyro4.locateNS()
    
    penerimaan = Pyro4.Proxy(ns.lookup("tepa.penerimaan"))
    penggajian = Pyro4.Proxy(ns.lookup("tepa.penggajian"))
    pelatihan = Pyro4.Proxy(ns.lookup("tepa.pelatihan"))
    
    nama = "John Doe"
    posisi = "Manajer"
    gaji_pokok = 5000000
    pelatihan_nama = "Manajemen Keuangan"
    
    lamaran = penerimaan.terima_lamaran(nama, posisi)
    print(lamaran)
    
    gaji = penggajian.hitung_gaji(nama, posisi, gaji_pokok)
    print(gaji)
    
    pelatihan_result = pelatihan.berikan_pelatihan(nama, posisi, pelatihan_nama)
    print(pelatihan_result)

if __name__ == "__main__":
    main()

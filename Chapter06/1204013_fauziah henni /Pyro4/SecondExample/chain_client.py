import Pyro4

def main():
    ns = Pyro4.locateNS()
    
    pemesanan = Pyro4.Proxy(ns.lookup("restoran.pemesanan"))
    pembayaran = Pyro4.Proxy(ns.lookup("restoran.pembayaran"))
    pengiriman = Pyro4.Proxy(ns.lookup("restoran.pengiriman"))
    
    menu = "Nasi Goreng"
    jumlah = 2
    alamat = "Jalan Raya No. 123"
    
    pesanan = pemesanan.pesan_menu(menu)
    print(pesanan)
    
    pembayaran_result = pembayaran.bayar_pesanan(menu, jumlah)
    print(pembayaran_result)
    
    pengiriman_result = pengiriman.kirim_pesanan(menu, alamat)
    print(pengiriman_result)

if __name__ == "__main__":
    main()

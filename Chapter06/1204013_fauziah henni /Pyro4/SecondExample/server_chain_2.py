import Pyro4

@Pyro4.expose
class Pembayaran(object):
    def bayar_pesanan(self, menu, jumlah):
        return "Pesanan {} dengan jumlah {} telah dibayar.".format(menu, jumlah)

daemon = Pyro4.Daemon()
uri = daemon.register(Pembayaran)

ns = Pyro4.locateNS()
ns.register("restoran.pembayaran", uri)

print("Server Pembayaran berjalan...")
daemon.requestLoop()

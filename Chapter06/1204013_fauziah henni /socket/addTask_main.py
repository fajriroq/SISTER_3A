import Pyro4

@Pyro4.expose
class Pengiriman(object):
    def kirim_pesanan(self, menu, alamat):
        return "Pesanan {} dikirim ke alamat: {}".format(menu, alamat)

daemon = Pyro4.Daemon()
uri = daemon.register(Pengiriman)

ns = Pyro4.locateNS()
ns.register("restoran.pengiriman", uri)

print("Server Pengiriman berjalan...")
daemon.requestLoop()

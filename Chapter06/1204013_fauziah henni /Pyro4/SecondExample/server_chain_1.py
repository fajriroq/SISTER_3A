import Pyro4

@Pyro4.expose
class Pemesanan(object):
    def pesan_menu(self, menu):
        return "Pesanan diterima: {}".format(menu)

daemon = Pyro4.Daemon()
uri = daemon.register(Pemesanan)

ns = Pyro4.locateNS()
ns.register("restoran.pemesanan", uri)

print("Server Pemesanan berjalan...")
daemon.requestLoop()

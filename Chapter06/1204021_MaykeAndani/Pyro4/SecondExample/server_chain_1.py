import Pyro4

@Pyro4.expose
class Penerimaan(object):
    def terima_lamaran(self, nama, posisi):
        return "Lamaran diterima: {} untuk posisi {}".format(nama, posisi)

daemon = Pyro4.Daemon()
uri = daemon.register(Penerimaan)

ns = Pyro4.locateNS()
ns.register("tepa.penerimaan", uri)

print("Server Penerimaan berjalan...")
daemon.requestLoop()

import Pyro4

@Pyro4.expose
class Penggajian(object):
    def hitung_gaji(self, nama, posisi, gaji_pokok):
        return "Gaji {} sebagai {} adalah {}".format(nama, posisi, gaji_pokok)

daemon = Pyro4.Daemon()
uri = daemon.register(Penggajian)

ns = Pyro4.locateNS()
ns.register("tepa.penggajian", uri)

print("Server Penggajian berjalan...")
daemon.requestLoop()

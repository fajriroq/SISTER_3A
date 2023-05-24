import Pyro4

@Pyro4.expose
class Pelatihan(object):
    def berikan_pelatihan(self, nama, posisi, pelatihan):
        return "Pelatihan {} untuk posisi {} adalah {}".format(nama, posisi, pelatihan)

daemon = Pyro4.Daemon()
uri = daemon.register(Pelatihan)

ns = Pyro4.locateNS()
ns.register("tepa.pelatihan", uri)

print("Server Pelatihan berjalan...")
daemon.requestLoop()

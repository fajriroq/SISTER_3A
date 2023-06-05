# server.py
import Pyro4
import time

@Pyro4.expose
class GreetingServer:
    def say_hello(self, name):
        return f"foo: Selamat Datang, {name}!"
    def do1(self,name):
        time.sleep(3)
        return f"foo: Sayonara, {name}"
    def do2(self,do2,name):
        time.sleep(3)
        if do2=="turu":
            return f"foo: Silahkan Keluar, {name}"
        else:
            return f"foo: okey, {name}"

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingServer)

print("Ready. Object uri =", uri)
daemon.requestLoop()

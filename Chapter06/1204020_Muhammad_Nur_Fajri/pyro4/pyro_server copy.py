# server.py
import Pyro4
import time

@Pyro4.expose
class GreetingServer:
    def say_hello(self, name):
        return f"foo: Apa Kareba, {name}!"
    def do1(self,name):
        time.sleep(3)
        return f"foo: Sarangeo, {name}"
    def do2(self,do2,name):
        time.sleep(3)
        if do2=="turu":
            return f"foo: Cordoba, {name}"
        else:
            return f"foo: Mantap, {name}"

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingServer)

print("Ready. Object uri =", uri)
daemon.requestLoop()

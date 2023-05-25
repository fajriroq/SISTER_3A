# client.py
import Pyro4

uri = input("gaddem uri dulu dong: ")


urname=input("ur name type sier: ")
gserver = Pyro4.Proxy(uri)
print(gserver.hello(urname))
print(gserver.saya(urname))
udoing=input("ur doing sier: ")
print(gserver.doc2(udoing,urname))

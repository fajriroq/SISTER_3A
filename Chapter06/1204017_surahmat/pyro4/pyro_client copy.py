# client.py
import Pyro4

uri = input("gaddem uri dulu dong: ")


urname=input("ur name type sier: ")
gserver = Pyro4.Proxy(uri)
print(gserver.say_hello(urname))
print(gserver.do1(urname))
udoing=input("ur doing sier: ")
print(gserver.do2(udoing,urname))

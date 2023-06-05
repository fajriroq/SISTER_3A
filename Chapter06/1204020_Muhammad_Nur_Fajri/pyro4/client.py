# client.py
import Pyro4

uri = input("masukkan uri terlebih dahulu: ")


urname=input("masukkan nama : ")
gserver = Pyro4.Proxy(uri)
print(gserver.say_hello(urname))
print(gserver.do1(urname))
udoing=input("selamat tinggal: ")
print(gserver.do2(udoing,urname))

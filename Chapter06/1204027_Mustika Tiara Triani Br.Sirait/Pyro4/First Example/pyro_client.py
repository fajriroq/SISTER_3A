import Pyro4

name = input("Siapa namanya ya ? ").strip()

server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))

import Pyro4

name = input("Siapa namamu wahai Traveler ? ").strip()

server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))

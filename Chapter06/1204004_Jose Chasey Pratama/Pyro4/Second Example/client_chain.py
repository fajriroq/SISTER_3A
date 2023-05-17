import Pyro4

name = input("Kota Awal ? ").strip()
obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.bandung")
print("Result=%s" % obj.process([name]))

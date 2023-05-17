import Pyro4


@Pyro4.expose
class Chain:
    def __init__(self, name: str, current_server: str):
        self.name = name
        self.current_serverName = current_server
        self.current_server = None

    def process(self, message):
        if self.current_server is None:
            self.current_server = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.current_serverName)
        if self.name in message:
            print(f"kembali ke {self.name} \n Perjalanan telah selesai")
            return [f"selesai pada {self.name}"]
        else:
            print(f"melanjutkan perjalanan dari {self.name} ke {self.current_serverName}")
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, f"telah melewati {self.name}")
            return result

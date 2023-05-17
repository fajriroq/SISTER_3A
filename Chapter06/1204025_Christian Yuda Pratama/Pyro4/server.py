import Pyro4

@Pyro4.expose
class ChatServer:
    def __init__(self):
        self.messages = []

    def send_message(self, username, message):
        self.messages.append((username, message))
        print("Menerima pesan dari", username + ":", message)

    def get_messages(self):
        return self.messages

daemon = Pyro4.Daemon()
uri = daemon.register(ChatServer)
name_server = Pyro4.locateNS()
name_server.register("chat.server", uri)

print("Server berjalan...")
daemon.requestLoop()

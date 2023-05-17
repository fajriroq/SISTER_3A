import Pyro4

uri = Pyro4.locateNS().lookup("chat.server")
server = Pyro4.Proxy(uri)

username = input("Masukkan nama pengguna: ")

while True:
    message = input("[" + username + "] Masukkan pesan (ketik 'q' untuk keluar): ")

    if message == 'q':
        break

    server.send_message(username, message)

    messages = server.get_messages()
    print("Pesan-pesan sebelumnya:")
    for username, message in messages:
        print("[" + username + "]:", message)

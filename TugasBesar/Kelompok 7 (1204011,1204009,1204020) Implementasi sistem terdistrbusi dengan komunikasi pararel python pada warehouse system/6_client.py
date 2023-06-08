from os import system, name
import socket
from datetime import date, datetime
import pickle

h_name = socket.gethostname()
IP_addr = socket.gethostbyname(h_name)
port = 9999
BUFFER_SIZE = 4096


def main():
    menu()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def send(command):
    log = {
        "ip_address": IP_addr,
        "date": date.today().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "activity": command[0],
        "value": command[1]
    }
    s = socket.socket()
    s.connect((h_name, port))
    base_log = pickle.dumps(log)
    s.send(base_log)
    data = s.recv(BUFFER_SIZE)
    data_decode = pickle.loads(data)
    s.close()
    return data_decode


def view_log():
    pilihan = input("""
1 : Lihat Semua Aktivitas
2 : Lihat Aktivitas Berdasarkan Tanggal
3 : Lihat Aktivitas Berdasarkan Jam
B : Kembali ke Menu Utama

Masukkan pilihan: """)
    clear()
    if pilihan.upper() == "1":
        print("Lihat Semua Aktivitas: ")
        value = send(['view log', None])
        num = 1
        for i in value:
            print("{}. IP Address: {}, Date: {}, Time: {}, Activity: {}, Value: {}".format(
                num, i['ip_address'], i['date'], i['time'], i['activity'], i['value']))
            num += 1
    elif pilihan.upper() == "2":
        print("Lihat Aktivitas Berdasarkan Tanggal")
        tgl = input("Masukkan Tanggal (ex: 22/06/2021): ")
        value = send(['log date', tgl])
        num = 1
        for i in value:
            print("{}. IP Address: {}, Date: {}, Time: {}, Activity: {}, Value: {}".format(
                num, i['ip_address'], i['date'], i['time'], i['activity'], i['value']))
            num += 1
    elif pilihan.upper() == "3":
        print("Lihat Aktivitas Berdasarkan Jam")
        jam = input("Masukkan Jam (ex: 17): ")
        value = send(['log hour', jam])
        num = 1
        for i in value:
            print("{}. IP Address: {}, Date: {}, Time: {}, Activity: {}, Value: {}".format(
                num, i['ip_address'], i['date'], i['time'], i['activity'], i['value']))
            num += 1
    elif pilihan.upper() == "B":
        menu()


def menu():
    while True:
        pilihan = input("""
V : Lihat Item
I : Tambah Item
E : Edit Item
D : Hapus Item
S : Lihat Aktivitas
Q : Keluar

Masukkan pilihan: """)
        clear()
        if pilihan.upper() == "V":
            print("Lihat Item: ")
            print(send(["view", None]))
        elif pilihan.upper() == "I":
            print("Tambah Item: ")
            add = input("Add New Item: ")
            print(send(["insert", add.lower()]))
        elif pilihan.upper() == "E":
            print("Edit Item: ")
            old = input("Item yang mau diganti: ")
            if send(["search", old.lower()]):
                new = input("Item baru: ")
                print(send(["update", [old.lower(), new.lower()]]))
            else:
                print(old, "not found")
        elif pilihan.upper() == "D":
            print("Hapus Item: ")
            deleted = input("Item yang mau dihapus: ")
            if send(["search", deleted.lower()]):
                print(send(["delete", deleted.lower()]))
            else:
                print(old, "not found")
        elif pilihan.upper() == "S":
            view_log()
        elif pilihan.upper() == "Q":
            break
        else:
            print("Pilihlah Sesuai Keyword")
            print("Masukkan Kembali Keyword")
            menu()


menu()
# print("Can not connect to server", TCP_IP)

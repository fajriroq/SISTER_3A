from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Daftar menu
    menu = {'Nasi Goreng': 15000, 'Mie Goreng': 12000, 'Nasi Padang': 20000, 'Sate Ayam': 25000}
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: {price} rupiah")

    # Mendapatkan pesanan dari pelanggan
    orders = []
    for i in range(size-1):
        order = random.choice(list(menu.keys()))
        orders.append(order)
        comm.send(order, dest=i+1)

    # Menghitung total harga pesanan
    total_price = 0
    for i in range(size-1):
        price = comm.recv(source=i+1)
        total_price += price
    print(f"Total harga pesanan: {total_price} rupiah")

else:
    # Menerima pesanan dari pelanggan
    order = comm.recv(source=0)

    # Menghitung harga pesanan
    menu = {'Nasi Goreng': 15000, 'Mie Goreng': 12000, 'Nasi Padang': 20000, 'Sate Ayam': 25000}
    price = menu[order]

    # Mengirim harga pesanan ke pelanggan
    comm.send(price, dest=0)
from mpi4py import MPI
import time


def check_stock(name, quantity):
    # Simulasi pengecekan stok obat
    print(f"Pengecekan stok obat {name} sebanyak {quantity} dimulai...")
    # Proses pengecekan stok obat berlangsung selama 3 detik
    time.sleep(3)
    stock = 10  # Jumlah stok obat tersedia saat ini
    if stock >= quantity:
        print(f"Stok obat {name} sebanyak {quantity} tersedia.")
    else:
        print(
            f"Stok obat {name} hanya tersedia {stock}. Transaksi tidak dapat dilakukan.")


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    print("My rank is:", rank)

    if rank == 0:
        name = "Paracetamol"
        quantity = 5
        destination_process = 4
        comm.send((name, quantity), dest=destination_process)
        print("Sending data", (name, quantity),
              "to process", destination_process)

    if rank == 1:
        name = "Amoxicillin"
        quantity = 10
        destination_process = 8
        comm.send((name, quantity), dest=destination_process)
        print("Sending data", (name, quantity),
              "to process", destination_process)

    if rank == 4:
        name, quantity = comm.recv(source=0)
        check_stock(name, quantity)

    if rank == 8:
        name, quantity = comm.recv(source=1)
        check_stock(name, quantity)

from mpi4py import MPI
import time

def rent_item(item, price):
    # Simulasi proses penyewaan barang
    print(f"Proses penyewaan {item} dengan harga {price} dimulai...")
    # Proses penyewaan berlangsung selama 2 detik
    time.sleep(2)
    print(f"Barang {item} berhasil disewakan dengan harga {price}")
    return price

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        items = [("TV", 100), ("Kulkas", 200), ("AC", 300)]
        for i, (item, price) in enumerate(items):
            destination_process = i+1
            comm.send((item, price), dest=destination_process)
            print(f"Sending data ({item}, {price}) to process {destination_process}...")

    else:
        item, price = comm.recv(source=0)
        rental_price = rent_item(item, price)
        comm.send(rental_price, dest=0)

    if rank == 0:
        total_rental_price = sum([comm.recv(source=i+1) for i in range(len(items))])
        print(f"Total biaya sewa: {total_rental_price}")

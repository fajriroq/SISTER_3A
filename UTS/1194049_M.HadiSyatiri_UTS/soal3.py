from mpi4py import MPI
import time

def crypto_transaction(sender, receiver, amount):
    # Simulasi proses transaksi kripto
    print(f"Proses transaksi kripto dengan jumlah {amount} oleh {sender} untuk {receiver} dimulai...")
    # Proses transaksi kripto berlangsung selama 2 detik
    time.sleep(2)
    print(f"Proses transaksi kripto dengan jumlah {amount} oleh {sender} untuk {receiver} selesai.")
    print(f"Transaksi kripto senilai {amount} berhasil dilakukan dari {sender} ke {receiver}.")

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    print("My rank is:", rank)

    if rank == 0:
        sender = 'John'
        receiver = 'Jane'
        amount = 10
        destination_process = 4
        comm.send((sender, receiver, amount), dest=destination_process)
        print("Sending data", (sender, receiver, amount), "to process", destination_process)

    if rank == 1:
        sender = 'Jane'
        receiver = 'John'
        amount = 5
        destination_process = 8
        comm.send((sender, receiver, amount), dest=destination_process)
        print("Sending data", (sender, receiver, amount), "to process", destination_process)

    if rank == 4:
        sender, receiver, amount = comm.recv(source=0)
        crypto_transaction(sender, receiver, amount)

    if rank == 8:
        sender, receiver, amount = comm.recv(source=1)
        crypto_transaction(sender, receiver, amount)

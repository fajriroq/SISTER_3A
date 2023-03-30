from mpi4py import MPI
import time 

def payment(amount, payment_method):
    # Simulasi proses pembayaran
    print(f"Proses pembayaran sebesar {amount} menggunakan {payment_method} dimulai...")
    # Proses pembayaran berlangsung selama 2 detik
    time.sleep(2)
    print(f"Proses pembayaran sebesar {amount} menggunakan {payment_method} selesai.")

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    print("My rank is:", rank)

    if rank == 0:
        amount = 50000
        payment_method = 'OVO'
        destination_process = 4
        comm.send((amount, payment_method), dest=destination_process)
        print("Sending data", (amount, payment_method), "to process", destination_process)

    if rank == 1:
        amount = 75000
        payment_method = 'GOPAY'
        destination_process = 8
        comm.send((amount, payment_method), dest=destination_process)
        print("Sending data", (amount, payment_method), "to process", destination_process)

    if rank == 4:
        amount, payment_method = comm.recv(source=0)
        payment(amount, payment_method)

    if rank == 8:
        amount, payment_method = comm.recv(source=1)
        payment(amount, payment_method)

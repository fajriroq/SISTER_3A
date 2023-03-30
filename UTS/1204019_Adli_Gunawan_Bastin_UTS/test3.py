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
    rank = comm.Get_rank()
    print("My rank is:", rank)

    if rank == 0:
        # Data untuk proses pembayaran rental mobil pertama
        amount = 50000
        payment_method = 'OVO'
        destination_process = 2

        # Kirim data ke proses tujuan
        comm.send((amount, payment_method), dest=destination_process)
        print(f"Process {rank} mengirim data {amount} dan {payment_method} ke process {destination_process}")

    if rank == 1:
        # Data untuk proses pembayaran rental mobil kedua
        amount = 75000
        payment_method = 'GOPAY'
        destination_process = 2

        # Kirim data ke proses tujuan
        comm.send((amount, payment_method), dest=destination_process)
        print(f"Process {rank} mengirim data {amount} dan {payment_method} ke process {destination_process}")

    if rank == 2:
        # Terima data dari process 0
        amount, payment_method = comm.recv(source=0)
        # Lakukan pembayaran rental mobil
        payment(amount, payment_method)
        # Terima data dari process 1
        amount, payment_method = comm.recv(source=1)
        # Lakukan pembayaran rental mobil
        payment(amount, payment_method)

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
        # Data untuk proses pembayaran rental mobil pertama
        amount = 50000
        payment_method = 'OVO'
        destination_process = 1

        # Kirim data ke proses tujuan
        comm.send((amount, payment_method), dest=destination_process)
        print(f"Process {rank} mengirim data {amount} dan {payment_method} ke process {destination_process}")

    if 0 < rank < 7:
        # Menerima data dari process sebelumnya
        amount, payment_method = comm.recv(source=rank-1)
        # Data untuk proses pembayaran rental mobil selanjutnya
        amount += 5000
        payment_method = 'DANA'
        destination_process = rank+1

        # Kirim data ke proses tujuan
        comm.send((amount, payment_method), dest=destination_process)
        print(f"Process {rank} menerima data {amount-5000} dan {payment_method} dari process {rank-1} dan mengirim data {amount} dan {payment_method} ke process {destination_process}")

    if rank == 7:
        # Menerima data dari process sebelumnya
        amount, payment_method = comm.recv(source=rank-1)
        # Lakukan pembayaran rental mobil
        payment(amount, payment_method)
        print(f"Process {rank} menerima data {amount} dan {payment_method} dari process {rank-1} dan melakukan pembayaran")


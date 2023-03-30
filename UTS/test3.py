from mpi4py import MPI
import time

def purchase(shoe_size, shoe_type, payment_method):
    # Simulasi proses pembelian sepatu
    print(f"Proses pembelian sepatu ukuran {shoe_size} tipe {shoe_type} menggunakan {payment_method} dimulai...")
    # Proses pembelian berlangsung selama 3 detik
    time.sleep(3)
    print(f"Proses pembelian sepatu ukuran {shoe_size} tipe {shoe_type} menggunakan {payment_method} selesai.")

if _name_ == '_main_':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    print("My rank is:", rank)

    if rank == 0:
        # Data untuk proses pembelian sepatu pertama
        shoe_size = 40
        shoe_type = 'Sneakers'
        payment_method = 'Credit Card'
        destination_process = 1

        # Kirim data ke proses tujuan
        comm.send((shoe_size, shoe_type, payment_method), dest=destination_process)
        print(f"Process {rank} mengirim data {shoe_size}, {shoe_type}, dan {payment_method} ke process {destination_process}")

    if 0 < rank < 7:
        # Menerima data dari process sebelumnya
        shoe_size, shoe_type, payment_method = comm.recv(source=rank-1)
        # Data untuk proses pembelian sepatu selanjutnya
        shoe_size += 1
        shoe_type = 'Boots'
        payment_method = 'PayPal'
        destination_process = rank+1

        # Kirim data ke proses tujuan
        comm.send((shoe_size, shoe_type, payment_method), dest=destination_process)
        print(f"Process {rank} menerima data {shoe_size-1}, {shoe_type}, dan {payment_method} dari process {rank-1} dan mengirim data {shoe_size}, {shoe_type}, dan {payment_method} ke process {destination_process}")

    if rank == 7:
        # Menerima data dari process sebelumnya
        shoe_size, shoe_type, payment_method = comm.recv(source=rank-1)
        # Lakukan pembelian sepatu
        purchase(shoe_size, shoe_type, payment_method)
        print(f"Process {rank} menerima data {shoe_size}, {shoe_type}, dan {payment_method} dari process {rank-1} dan melakukan pembelian")
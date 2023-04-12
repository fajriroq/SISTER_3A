from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    nama = input("Masukkan nama peserta: ")
    umur = int(input("Masukkan umur peserta: "))
    alamat = input("Masukkan alamat peserta: ")

    # PTPC
    comm.send(nama, dest=1)
    comm.send(umur, dest=1)
    comm.send(alamat, dest=1)

else:
    # PTPC
    nama = comm.recv(source=0)
    umur = comm.recv(source=0)
    alamat = comm.recv(source=0)

# collective communication
umur = comm.bcast(umur, root=0)

# Membuat topologi 2D
cart_comm = comm.Create_cart((2, 2), periods=(True, True), reorder=True)

# collective communication
umur_arr = np.array(umur)
umur_sum = np.zeros(1)
cart_comm.Reduce(umur_arr, umur_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Proses pendaftaran selesai. Jumlah peserta yang terdaftar: {umur_sum[0]}")

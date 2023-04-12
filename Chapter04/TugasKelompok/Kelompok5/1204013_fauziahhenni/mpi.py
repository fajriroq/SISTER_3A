from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Inisialisasi data makanan dan minuman
if rank == 0:
    makanan = ["Nasi Goreng", "Mie Goreng", "Bakso", "Sate"]
    minuman = ["Es Teh", "Es Jeruk", "Jus Alpukat", "Jus Mangga"]
else:
    makanan = None
    minuman = None

# Broadcast data makanan dan minuman ke semua proses
makanan = comm.bcast(makanan, root=0)
minuman = comm.bcast(minuman, root=0)

# Pesanan pelanggan
pesanan_makanan = random.choice(makanan)
pesanan_minuman = random.choice(minuman)

# Kumpulkan pesanan makanan dan minuman dari semua proses
data_pesanan = comm.gather((pesanan_makanan, pesanan_minuman), root=0)

# Tampilkan hasil pesanan dari semua pelanggan
if rank == 0:
    print("Pesanan pelanggan:")
    for i in range(size):
        print(f"Pelanggan {i+1}: Makanan = {data_pesanan[i][0]}, Minuman = {data_pesanan[i][1]}")
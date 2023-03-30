from mpi4py import MPI
import random

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Split komunikator MPI menjadi beberapa grup dengan nilai rank yang acak
rand = random.randint(0, 100)
color = rand % 2
newcomm = comm.Split(color, rank)

# List nama barang yang mungkin dikirim
nama_barang = ['Laptop', 'Smartphone', 'Tablet', 'Kamera', 'Headset']

# Data barang yang akan dikirim
barang = None
if newcomm.Get_rank() == 0:
    barang = {'nama': random.choice(
        nama_barang), 'jumlah': random.randint(1, 10)}

# Kirim data barang dari rank 0 ke seluruh rank lainnya
barang = newcomm.bcast(barang, root=0)

# Proses pengiriman barang di setiap rank
if newcomm.Get_rank() != 0:
    print(
        f"Vendor {newcomm.Get_rank()}: Mengirim {barang['jumlah']} {barang['nama']}")

# Terima konfirmasi pengiriman dari seluruh rank
konfirmasi = newcomm.allgather(
    f"Pengiriman {barang['jumlah']} {barang['nama']} berhasil")

# Menampilkan hasil konfirmasi di rank 0
if newcomm.Get_rank() == 0:
    for i in range(newcomm.Get_size()):
        print(konfirmasi[i])

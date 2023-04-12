from mpi4py import MPI

# inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# data barang
stok = {'stok sendok': 100, 'stok piring': 200, 'stok pisau': 300}

# menghitung subtotal tagihan
subtotal = 0
for item in stok.values():
    subtotal += item

# menghitung total tagihan dengan mengumpulkan subtotal dari semua proses
total = comm.allreduce(subtotal, op=MPI.SUM)

# mencetak tagihan untuk setiap proses
if rank == 0:
    print(f'Total stok: {total}')
for item, price in stok.items():
    print(f'Stok kosong {rank}: {item} = {price}')

# menghitung rata-rata tagihan
avg = total / size

# mencetak rata-rata tagihan jika proses adalah root (proses dengan rank 0)
if rank == 0:
    print(f'Rata-rata stok: {avg}')

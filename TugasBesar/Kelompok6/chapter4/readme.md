Import modul MPI dari mpi4py. = from mpi4py import MPI

Membuat communicator comm menggunakan MPI.COMM_WORLD yang mewakili seluruh komunikator MPI yang sedang berjalan. = 
comm = MPI.COMM_WORLD

Mendapatkan rank (peringkat) dan size (jumlah total proses) dari communicator. = 
rank = comm.Get_rank()
size = comm.Get_size()

Mendefinisikan dictionary items yang berisi informasi persediaan barang dengan nama barang sebagai kunci dan jumlah persediaan sebagai nilai. = items = {'Radio tersedia': 100, 'Tv tersedia': 200, 'Laptop': 300}

Menghitung subtotal dengan menjumlahkan semua nilai persediaan barang dari items. = 
subtotal = 0
for item in items.values():
    subtotal += item

Menggunakan comm.allreduce() untuk melakukan operasi reduksi pada subtotal dengan operasi penjumlahan (MPI.SUM). Hasilnya akan disimpan dalam variabel total di semua proses. = 
total = comm.allreduce(subtotal, op=MPI.SUM)

Jika rank proses adalah 0, mencetak total barang terjual dengan menggunakan print(). =
if rank == 0:
    print(f'Total Barang Terjual: {total}')

Menggunakan loop for untuk mencetak informasi persediaan barang dan harga dari items di setiap proses. Informasi ini mencakup rank proses, nama barang, dan harga. = 
for item, price in items.items():
    print(f'Persediaan {rank}: {item} - {price}')

Menghitung rata-rata barang terjual dengan membagi total dengan size (jumlah total proses). Hanya jika rank proses adalah 0, mencetak rata-rata barang terjual. =
avg = total / size
if rank == 0:
    print(f'Rata-rata barang terjual : {avg}')


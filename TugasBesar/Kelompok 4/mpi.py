from mpi4py import MPI

# Data karyawan
karyawan = [
    {"nama": "Mayke Andani", "usia": 22, "posisi": "Staff", "gaji": 5000000, "masa_jabatan": "2 tahun"},
    {"nama": "Wulan Nur", "usia": 21, "posisi": "Staff", "gaji": 6000000, "masa_jabatan": "2 tahun"},
    {"nama": "Nurul", "usia": 30, "posisi": "Manager", "gaji": 5000000, "masa_jabatan": "5 tahun"},
    {"nama": "Fauziah", "usia": 35, "posisi": "Supervisor", "gaji": 4500000, "masa_jabatan": "3 tahun"},
    {"nama": "Rama", "usia": 28, "posisi": "Staff", "gaji": 3200000, "masa_jabatan": "1 tahun"},
    {"nama": "Sinta", "usia": 32, "posisi": "Manager", "gaji": 4800000, "masa_jabatan": "4 tahun"}
]

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Jumlah karyawan yang akan diproses oleh setiap proses
karyawan_per_process = len(karyawan) // size

# Menghitung gaji karyawan berdasarkan posisi
def hitung_gaji(karyawan):
    posisi = karyawan['posisi']
    gaji = karyawan['gaji']
    
    if posisi == 'Staff':
        gaji *= 1.1
    elif posisi == 'Manager':
        gaji *= 1.2
    elif posisi == 'Supervisor':
        gaji *= 1.3
    
    return gaji

# Proses master (rank 0)
if rank == 0:
    total_gaji = 0
    
    # Menghitung gaji untuk karyawan pada proses master
    for i in range(karyawan_per_process):
        karyawan_index = i
        gaji = hitung_gaji(karyawan[karyawan_index])
        total_gaji += gaji

    # Mengumpulkan total gaji dari semua proses
    for i in range(1, size):
        gaji = comm.recv(source=i)
        total_gaji += gaji

    print("Total gaji: ", total_gaji)

# Proses lainnya
else:
    total_gaji = 0

    # Menghitung gaji untuk karyawan pada proses tersebut
    for i in range(rank * karyawan_per_process, (rank + 1) * karyawan_per_process):
        karyawan_index = i
        gaji = hitung_gaji(karyawan[karyawan_index])
        total_gaji += gaji

    # Mengirimkan total gaji ke proses master
    comm.send(total_gaji, dest=0)

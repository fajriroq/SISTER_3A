from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

jadwal_kuliah = [
    ["Sistem Tersebar", "Sitem Multimedia"],
    ["AI","Bahasa Inggris"],
    ["Statitistika", "Data Mining"]
]

if rank == 0:
    for i in range(1, size):
        comm.send(jadwal_kuliah, dest=i)
else:
    jadwal = comm.recv(source=0)

    print("Jadwal kuliah untuk mahasiswa dengan rank ", rank)
    for i in range(len(jadwal)):
        print(jadwal[i])

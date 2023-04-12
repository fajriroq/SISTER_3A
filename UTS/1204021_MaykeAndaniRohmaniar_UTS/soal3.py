from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    n = 5  
    donatur = [("John", 10000), ("Jane", 20000), ("Bob", 5000), ("Alice", 15000), ("Peter", 30000)]  
else:
    donatur = None
    n = None


donatur = comm.bcast(donatur, root=0)
n = comm.bcast(n, root=0)
total_donasi = sum([x[1] for x in donatur])
rata_donasi = total_donasi / n
data_total_rata_donasi = comm.gather((total_donasi, rata_donasi), root=0)


if rank == 0:
    print("Data total dan rata-rata donasi:")
    for i in range(size):
        print(f"Proses donasi {i}: Total donasi = {data_total_rata_donasi[i][0]}, Rata-rata donasi = {data_total_rata_donasi[i][1]}")

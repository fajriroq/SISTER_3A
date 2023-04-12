from mpi4py import MPI
import time

def sort_palm_oil(palm_oil_list):
    # Simulasi proses penyortiran kelapa sawit
    print(f"Proses penyortiran kelapa sawit dimulai...")
    # Proses penyortiran kelapa sawit berlangsung selama 5 detik
    time.sleep(5)
    palm_oil_list.sort()
    print(f"Proses penyortiran kelapa sawit selesai. Hasil: {palm_oil_list}")

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    print("My rank is:", rank)

    if rank == 0:
        palm_oil_list = [5, 3, 8, 1, 6]
        destination_process = 4
        comm.send(palm_oil_list, dest=destination_process)
        print("Sending data", palm_oil_list, "to process", destination_process)

    if rank == 1:
        palm_oil_list = [7, 4, 2, 9, 0]
        destination_process = 8
        comm.send(palm_oil_list, dest=destination_process)
        print("Sending data", palm_oil_list, "to process", destination_process)

    if rank == 4:
        palm_oil_list = comm.recv(source=0)
        sort_palm_oil(palm_oil_list)

    if rank == 8:
        palm_oil_list = comm.recv(source=1)
        sort_palm_oil(palm_oil_list)

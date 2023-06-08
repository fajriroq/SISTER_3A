from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def book_ticket(concert):
    for ticket in concert:
        print("Process {} - Booking ticket:".format(rank))
        print("Concert:", ticket[0])
        print("Date:", ticket[1])
        print("Seat:", ticket[2])
        print()

concerts = [
    ["Artist 1 Concert", "2023-07-01", "A1"],
    ["Artist 2 Concert", "2023-07-02", "B2"],
    ["Artist 3 Concert", "2023-07-03", "C3"],
]

if rank == 0:
    for i in range(1, size):
        comm.send(concerts, dest=i)
else:
    concert_data = comm.recv(source=0)

    print("Ticket booking for process rank", rank)
    book_ticket(concert_data)

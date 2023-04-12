from mpi4py import MPI
import time 

def borrow_book(book_id, borrower_name):
    # Simulasi proses peminjaman buku
    print(f"Proses peminjaman buku dengan ID {book_id} oleh {borrower_name} dimulai...")
    # Proses peminjaman buku berlangsung selama 5 detik
    time.sleep(2)
    print(f"Proses peminjaman buku dengan ID {book_id} oleh {borrower_name} selesai.")

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    print("My rank is:", rank)

    if rank == 0:
        book_id = 'B001'
        borrower_name = 'John'
        destination_process = 4
        comm.send((book_id, borrower_name), dest=destination_process)
        print("Sending data", (book_id, borrower_name), "to process", destination_process)

    if rank == 1:
        book_id = 'B002'
        borrower_name = 'Jane'
        destination_process = 8
        comm.send((book_id, borrower_name), dest=destination_process)
        print("Sending data", (book_id, borrower_name), "to process", destination_process)

    if rank == 4:
        book_id, borrower_name = comm.recv(source=0)
        borrow_book(book_id, borrower_name)

    if rank == 8:
        book_id, borrower_name = comm.recv(source=1)
        borrow_book(book_id, borrower_name)

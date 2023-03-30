import multiprocessing
import time

def borrow(lawan_id, borrower_id):

    time.sleep(1)
    print(f"Anggota {borrower_id} telah bertanding dengan  lawan ID {lawan_id}")

def return_lawan(lawan_id, borrower_id):

    time.sleep(1)
    print(f"Anggota {borrower_id} telah mengalahkan lawan dengan ID {lawan_id}")

def spawn(func, args):
    # Spawning child process
    p = multiprocessing.Process(target=func, args=args)
    p.start()
    p.join()

if __name__ == '__main__':

    lawan_catalogue = ["ARNOLD LATO LATO"]

    # Parent process
    print("Parent process started")

    spawn(borrow, (1, 'JORDAN'))

    spawn(return_lawan, (1, 'JORDAN'))

    # Tampilkan katalog lawan setelah peminjaman dan pengembalian
    print(f"PEMAIN TELAH MENGALAHKAN : {lawan_catalogue[0]}")

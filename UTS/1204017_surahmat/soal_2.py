import multiprocessing
import time

def borrow(book_id, borrower_id):
    # Simulasi proses peminjaman buku
    time.sleep(1)
    print(f"Anggota {borrower_id} telah meminjam buku dengan ID {book_id}")

def return_book(book_id, borrower_id):
    # Simulasi proses pengembalian buku
    time.sleep(1)
    print(f"Anggota {borrower_id} telah mengembalikan buku dengan ID {book_id}")

if __name__ == '__main__':
    # Katalog buku
    book_catalogue = [1, 2, 3, 4, 5]

    # Proses peminjaman buku
    borrow_process = multiprocessing.Process(target=borrow, args=(1, 'A001'))
    borrow_process.start()

    # Proses pengembalian buku
    return_process = multiprocessing.Process(target=return_book, args=(1, 'A001'))
    return_process.start()

    # Tunggu sampai kedua proses selesai
    borrow_process.join()
    return_process.join()
    

    # Tampilkan katalog buku setelah peminjaman dan pengembalian
    print(f"Katalog buku setelah peminjaman dan pengembalian: {book_catalogue}")

import multiprocessing
import time

def calculate_total_price(book_price, qty, tax_rate):
    subtotal = book_price * qty
    tax = subtotal * (tax_rate/100)
    total_price = subtotal + tax
    return total_price

if __name__ == '__main__':
    # Inisialisasi data buku
    book_title = "Python for Data Science"
    book_price = 150000
    qty = 2
    tax_rate = 10
    
    # Memulai proses multiprocessing
    start_time = time.time()
    pool = multiprocessing.Pool()
    results = []
    
    # Menambahkan proses ke dalam pool
    results.append(pool.apply_async(calculate_total_price, args=(book_price, qty, tax_rate)))
    results.append(pool.apply_async(calculate_total_price, args=(book_price, qty+1, tax_rate)))
    results.append(pool.apply_async(calculate_total_price, args=(book_price, qty+2, tax_rate)))
    
    # Menutup pool dan menunggu proses selesai
    pool.close()
    pool.join()
    
    # Mengambil hasil dari setiap proses
    total_prices = [r.get() for r in results]
    total_price = sum(total_prices)
    
    # Output hasil perhitungan
    print("Book title: ", book_title)
    print("Book price: ", book_price)
    print("Quantity: ", qty)
    print("Tax rate: ", tax_rate, "%")
    print("Total price: ", total_price)
    print("Execution time: ", time.time()-start_time, " seconds")

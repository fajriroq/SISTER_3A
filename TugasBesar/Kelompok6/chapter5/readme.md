Import modul asyncio. = import asyncio

Mendefinisikan coroutine factorial(number) yang akan menghitung faktorial dari suatu angka. Coroutine ini menggunakan loop for untuk mengiterasi dari 2 hingga angka yang diberikan. Pada setiap iterasi, mencetak informasi "Tv Terjual Sebanyak (i)", melakukan jeda menggunakan asyncio.sleep(1), dan mengakumulasi hasil faktorial dalam variabel fact. Setelah iterasi selesai, mencetak hasil faktorial. = 
@asyncio.coroutine
def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Tv Terjual Sebanyak (%s)' % i)
        yield from asyncio.sleep(1)
        fact *= i
    print('Jumlah Tv Terjual (%s) = %s' % (number, fact))

Mendefinisikan coroutine fibonacci(number) yang akan menghasilkan deret Fibonacci. Coroutine ini menggunakan loop for untuk mengiterasi sebanyak number. Pada setiap iterasi, mencetak informasi "Laptop Terjual Sebanyak (i)", melakukan jeda menggunakan asyncio.sleep(1), dan menghitung nilai Fibonacci dengan mengubah nilai a dan b. Setelah iterasi selesai, mencetak nilai Fibonacci terakhir. = 
@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Laptop Terjual Sebanyak (%s)' % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print('Jumlah Laptop Terjual (%s) = %s' % (number, a))

Mendefinisikan coroutine binomial_coefficient(n, k) yang akan menghitung koefisien binomial. Coroutine ini menggunakan loop for untuk mengiterasi dari 1 hingga k. Pada setiap iterasi, mencetak informasi "Produk Tersisa (i)", melakukan jeda menggunakan asyncio.sleep(1), dan menghitung nilai koefisien binomial. Setelah iterasi selesai, mencetak hasil koefisien binomial. =
@asyncio.coroutine
def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print('Produk Tersisa (%s)' % i)
        yield from asyncio.sleep(1)
    print('Jumlah Semua Barang Yang Terjual (%s, %s) = %s' % (n, k, result))
    
Memeriksa apakah kode ini dijalankan sebagai program utama menggunakan if __name__ == '__main__':. Hal ini diperlukan dalam penggunaan modul asyncio. = 
if __name__ == '__main__':
Membuat list task_list yang berisi tiga task asyncio, masing-masing untuk menjalankan coroutine factorial(10),
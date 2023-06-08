import asyncio


@asyncio.coroutine
def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Tv Terjual Sebanyak (%s)' % i)
        yield from asyncio.sleep(1)
        fact *= i
    print('Jumlah Tv Terjual (%s) = %s' % (number, fact))


@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Laptop Terjual Sebanyak (%s)' % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print('Jumah Laptop Terjual (%s) = %s' % (number, a))


@asyncio.coroutine
def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        print('Produk Tersisa (%s)' % i)
        yield from asyncio.sleep(1)
    print('Jumlah Semua Barang Yang Terjual (%s, %s) = %s' % (n, k, result))


if __name__ == '__main__':
    task_list = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomial_coefficient(20, 10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()

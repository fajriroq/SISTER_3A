import multiprocessing


def barang(i):
    print('Jumlah barang yang harus dikirimkan: %s' % i)
    for j in range(0, i):
        print('Jumlah Barang yang telah selesai dikirimkan :%s' % j)
    return


if __name__ == '__main__':
    for i in range(3):
        process = multiprocessing.Process(target=barang, args=(i,))
        process.start()
        process.join()

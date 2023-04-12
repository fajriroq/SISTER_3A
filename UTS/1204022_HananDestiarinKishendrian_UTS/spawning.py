import multiprocessing

def myFunc(i):
    print ('Terdapat stok kosong: %s' %i)
    for j in range (0,i):
        print('Re-stok barang :%s' %j)
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
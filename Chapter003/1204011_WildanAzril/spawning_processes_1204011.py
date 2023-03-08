import multiprocessing

def myFunc(i):
    print ('Proses data akan dimulai dari: %s' %i)
    for j in range (1,i):
        print('Data yang berhasil di akses :%s' %j)
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
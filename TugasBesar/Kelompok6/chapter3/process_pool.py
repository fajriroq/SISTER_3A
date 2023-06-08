import multiprocessing
from time import ctime, sleep
from random import random

def function_square(data):
    result = data*data
    return result

barang1 = 'Tv'
barang2 = 'Radio'
barang3 = 'Laptop'
if __name__ == '__main__':
    inputs1 = list(range(8,9))
    inputs2 = list(range(10,11))
    inputs3 = list(range(20,21))
    
    pool = multiprocessing.Pool(processes=4)
    pool_outputs1 = pool.map(function_square, inputs1)
    pool_outputs2 = pool.map(function_square, inputs2)
    pool_outputs3 = pool.map(function_square, inputs3)
    
    terjual1 = barang1
    terjual2 = barang2
    terjual3 = barang3
    
    value = random() * 5
    sleep(value)
    
    print (f'Barang Terjual: \nNama Barang: %s \nNomor Barang: %s \nWaktu : {value} \nTanggal: %s \n' % (terjual1, pool_outputs1, ctime()))
    print (f'Barang Terjual: \nNama Barang: %s \nNomor Barang: %s \nWaktu : {value} \nTanggal: %s \n' % (terjual2, pool_outputs2, ctime()))
    print (f'Barang Terjual: \nNama Barang: %s \nNomor Barang: %s \nWaktu : {value} \nTanggal: %s \n' % (terjual3, pool_outputs3, ctime()))
    
    pool.close() 
    pool.join()  

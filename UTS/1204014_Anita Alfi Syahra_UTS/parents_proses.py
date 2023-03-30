import os
import multiprocessing
import time

def hitung_rata_rata(nilai):
    total = 0
    for n in nilai:
        total += n
    rata_rata = total / len(nilai)
    return rata_rata

def tentukan_grade(rata_rata):
    if rata_rata >= 80:
        return 'A'
    elif rata_rata >= 70:
        return 'B'
    elif rata_rata >= 60:
        return 'C'
    elif rata_rata >= 50:
        return 'D'
    else:
        return 'E'

def tulis_ke_file(nama_file, nama, nilai):
    with open(nama_file, 'a') as f:
        f.write(nama + '\n')
        f.write(str(nilai) + '\n')

if __name__ == '__main__':
  
    nama_file = 'data_mahasiswa.txt'
    if os.path.exists(nama_file):
        os.remove(nama_file)

    while True:
        nama = input('Masukkan nama mahasiswa: ')
        if nama == '':
            break
        nilai = []
        while True:
            n = input('Masukkan nilai (ketik "selesai" untuk mengakhiri): ')
            if n == 'selesai':
                break
            nilai.append(int(n))

        rata_rata = hitung_rata_rata(nilai)
        grade = tentukan_grade(rata_rata)

        tulis_ke_file(nama_file, nama, nilai)

        print('Rata-rata nilai:', rata_rata)
        print('Grade:', grade)

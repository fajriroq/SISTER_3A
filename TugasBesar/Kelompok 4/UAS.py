import multiprocessing
import asyncio

# Fungsi untuk menghitung gaji karyawan
def hitung_gaji(karyawan, condition):
    with condition:
        print(f'Menghitung gaji untuk karyawan {karyawan}')
        condition.wait()  # Menunggu persetujuan dari pengelola
        print(f'{karyawan} menerima gaji')
        condition.notify()  # Memberi tahu pengelola bahwa proses selesai

# Fungsi untuk pengelola gaji
def pengelola_gaji(condition):
    with condition:
        print('Pengelola mengeluarkan gaji')
        condition.notify_all()  # Memberi tahu karyawan-karyawan yang sedang menunggu persetujuan

if __name__ == '__main__':
    condition = multiprocessing.Condition()  # Membuat objek Condition

    # Daftar karyawan
    karyawan = ['Wulan', 'Mayke', 'Nurul', 'Fauziah', 'Rama', 'Sinta']

    processes = []
    for i, nama in enumerate(karyawan):
        p = multiprocessing.Process(target=hitung_gaji, args=(nama, condition))
        processes.append(p)
        p.start()

    asyncio.run(asyncio.sleep(2))  # Menunggu sebentar sebelum pengelola mengeluarkan gaji

    pengelola = multiprocessing.Process(target=pengelola_gaji, args=(condition,))
    pengelola.start()

    for p in processes:
        p.join()  # Menunggu semua proses selesai

    with condition:
        condition.notify()  # Memberi tahu pengelola bahwa semua proses selesai

    pengelola.join()  # Menunggu proses pengelola selesai

    print('Semua proses selesai')

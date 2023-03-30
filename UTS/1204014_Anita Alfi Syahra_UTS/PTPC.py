from mpi4py import MPI
import time
import multiprocessing

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

def pemrosesan_data(nama, nilai, rank):
  
    rata_rata = hitung_rata_rata(nilai)
    grade = tentukan_grade(rata_rata)

    
    nama_file = 'data_mahasiswa.txt'
    tulis_ke_file(nama_file, nama, nilai)

    print('Rank', rank, '- Rata-rata nilai:', rata_rata)
    print('Rank', rank, '- Grade:', grade)

def create_topologies(comm):
    
    cart_comm = comm.Create_cart((2, 2), periods=(False, False), reorder=False)
    graph_comm = comm.Create_graph([(0, 1), (1, 2), (2, 3), (3, 0)])

    print('Cartesian topology:', cart_comm.Get_topo())
    print('Graph topology:', graph_comm.Get_topo())

    return comm, cart_comm, graph_comm

if __name__ == '__main__':
    
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    nama_file = 'data_mahasiswa.txt'
    f = open(nama_file, 'w')
    f.close()

    data = []
    if rank == 0:
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

            data.append((nama, nilai))

    # melakukan pemrosesan data secara linear di rank 0

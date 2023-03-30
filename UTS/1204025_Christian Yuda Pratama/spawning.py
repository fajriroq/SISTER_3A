import multiprocessing

def process_jobdesk(pegawai, jobdesk):
    jumlah_pekerjaan = len(jobdesk)
    print("Pegawai {} memiliki {} pekerjaan".format(pegawai, jumlah_pekerjaan))

if __name__ == '__main__':
    data_pegawai = {
        'Yuda': ['Menyelesaikan Laporan', 'Membuat Presentasi'],
        'Adi': ['Membuat  Program Aplikasi Komputer', 'Menguji program yang telah dibuat untuk memastikan kinerja yang baik',' mengembangkan program aplikasi komputer','Menyusun Aplikasi Strategi Pemasaran'],
        'Jose': ['Membuat Aplikasi Surat', 'membuat aplikasi  Jadwal Rapat', 'Membuat sebuah aplikasi kedokteran'],
        'Hanan': ['Membuat Aplikasi Laporan Keuangan'],
    }
    proses = []
    for pegawai, jobdesk in data_pegawai.items():
        p = multiprocessing.Process(target=process_jobdesk, args=(pegawai, jobdesk))
        proses.append(p)
        p.start()
    for p in proses:
        p.join()
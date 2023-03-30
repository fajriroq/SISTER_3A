import multiprocessing
import time

def hitung_gaji(nama, gaji_perjam, jam_kerja):
    gaji = gaji_perjam * jam_kerja
    print(f"{nama} bekerja selama {jam_kerja} jam dan mendapatkan gaji sebesar {gaji}.")
    time.sleep(1) 

if __name__ == "__main__":
    daftar_pekerja = [("YUDA", 10000), ("ADI", 10000), ("JOSE", 50000)]
    proses_pekerja = []
    for pekerja in daftar_pekerja:
        nama = pekerja[0]
        gaji_perjam = pekerja[1]
        proses = multiprocessing.Process(target=hitung_gaji, args=(nama, gaji_perjam, 8))
        proses_pekerja.append(proses)
        
    for proses in proses_pekerja:
        proses.start()
        time.sleep(1)

    for proses in proses_pekerja:
        proses.join()
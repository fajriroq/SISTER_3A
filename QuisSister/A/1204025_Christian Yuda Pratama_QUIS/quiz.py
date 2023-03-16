import threading
import time
from queue import Queue

def hitung_gaji_pegawai(pegawai, waktu_kerja_dict, lock, q):
    with lock:
        print(f"Memulai penggajian untuk {pegawai}...")
    gaji = 3000000 
    waktu_kerja = waktu_kerja_dict[pegawai] 
    honor = 0
    if waktu_kerja > 8: 
        honor = (waktu_kerja - 8) * 100000
    total_gaji = gaji + honor
    print(f"{pegawai} bekerja selama {waktu_kerja} jam")
    print(f"{pegawai} mendapatkan gaji sebesar Rp{gaji} dan honor sebesar Rp{honor}")
    print(f"Total gaji {pegawai} adalah Rp{total_gaji}")
    q.put(total_gaji)
    time.sleep(1)

if __name__ == '__main__':
    daftar_pegawai = {
        "Yuda": 12,
        "Adi": 6,
        "Hanan": 9,
        "Jose": 9,
        "Mayke": 9,
        "Fira": 9,
        "Wulan": 9,
        "Dani": 9,
        "Budi": 9
    }

    lock = threading.Lock()

    threads = []
    q = Queue() 
    for pegawai in daftar_pegawai:
        t = threading.Thread(target=hitung_gaji_pegawai, args=(pegawai, daftar_pegawai, lock, q))
        threads.append(t)

    time.sleep(3)

    start_time = time.time() 
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    total_gaji = 0
    while not q.empty():
        total_gaji += q.get()

    print(f"Total gaji seluruh pegawai adalah Rp{total_gaji}")

    end_time = time.time()
    total_time = end_time - start_time
    minutes, seconds = divmod(total_time, 60)
    print(f"Proses penggajian dan honor telah selesai dalam waktu {int(minutes)} menit {seconds:.2f} detik.")

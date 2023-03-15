import ntplib
import time

if __name__ == "__main__":
    # Inisialisasi waktu awal
    start_time = time.time()

    # Mendapatkan waktu dari server lokal
    local_time = time.time()

    # Mendapatkan waktu dari server lain
    ntp_server = '0.pool.ntp.org'
    ntp_client = ntplib.NTPClient()
    ntp_response = ntp_client.request(ntp_server, version=3)
    remote_time = ntp_response.tx_time

    # Menentukan selisih waktu antara server lokal dan server lain
    time_difference = remote_time - time.time()

    # Menghitung waktu akhir dengan menambahkan selisih waktu ke waktu lokal

    end_time = local_time + time_difference
    # Menampilkan hasil sinkronisasi waktu
    print("Waktu awal : ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print("Waktu lokal: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(local_time)))
    print("Waktu remote: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(remote_time)))
    print("Selisih waktu: %.6f detik" % time_difference)
    print("Waktu sinkronisasi: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))

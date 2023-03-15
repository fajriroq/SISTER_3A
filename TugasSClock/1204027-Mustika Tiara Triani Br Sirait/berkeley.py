import time
import random


def berkeley_algorithm(trip_times):                  
    sorted_trip_times = sorted(trip_times)
    median_time = sorted_trip_times[len(sorted_trip_times) // 2]
    return median_time - time.time()                   

# Fungsi untuk melakukan trip time ke mesin lain
def trip_time(remote_host):
    return time.time() - random.uniform(0, 1)

# Daftar mesin di dalam jaringan
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Inisialisasi trip times
trip_times = [trip_time(host) for host in hosts]        

# Hitung offset waktu
berkeley = berkeley_algorithm(trip_times)                   

# Atur waktu lokal
local_time = time.time() + berkeley
print("Waktu lokal sekarang:", time.ctime(local_time))  

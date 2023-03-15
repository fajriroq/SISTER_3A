# algoritma Berkeley biasanya memerlukan setidaknya dua perangkat untuk melakukan sinkronisasi waktu yang akurat.

import socket
import struct
import time

def berkeley_algorithm(server_address_list):
    # Sambungkan ke server NTP dan dapatkan waktunya
    socket_list = []
    for server_address in server_address_list:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(b'\x1b' + 47 * b'\0', server_address)
        data, server = client_socket.recvfrom(1024)
        t = struct.unpack('!12I', data)[10]
        t -= 2208988800  # convert to Unix time
        socket_list.append((client_socket, t))
    
    # Hitung perbedaan waktu rata-rata antara jam lokal dan server NTP
    local_time = time.time()
    time_difference = 0
    for client_socket, t in socket_list:
        time_difference += t - local_time
        client_socket.close()
    time_difference /= len(socket_list)
    
    # Sesuaikan jam lokal menggunakan perbedaan waktu rata-rata
    adjusted_time = local_time + time_difference
    return adjusted_time                            

if __name__ == '__main__':
    # dua server NTP
    server_address_list = [('pool.ntp.org', 123), ('time.windows.com', 123)]
    adjusted_time = berkeley_algorithm(server_address_list)
    print(f'Jam lokal disesuaikan dengan {adjusted_time - time.time():.3f} detik')

import socket
import struct
import time

NTP_SERVER = '0.id.pool.ntp.org'
NTP_PORT = 123


def get_ntp_time(self):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (NTP_SERVER, NTP_PORT))
    data, address = client.recvfrom(1024)
    if data:
        ntp_time = struct.unpack('!12I', data)[10]
        ntp_time -= 2208988800
        return ntp_time


def cristian_sync_time(ntp_servers):
    ntp_time = get_ntp_time(ntp_servers[0])
    t1 = time.time()
    t2 = get_ntp_time(ntp_servers[1])
    t3 = time.time()

    corrected_time = t2 + (t3 - t1) / 2 - ntp_time

    print('System time before correction:', time.ctime(time.time()))
    print('System time after correction:',
          time.ctime(time.time() + corrected_time))


def calculate_delivery_time(distance, speed):
    cristian_sync_time(['0.id.pool.ntp.org', '1.id.pool.ntp.org'])
    current_time = time.time()
    time_to_delivery = distance / speed
    delivery_time = current_time + time_to_delivery
    print('Delivery time:', time.ctime(delivery_time))


calculate_delivery_time(100, 60)
# jarak 100 km, kecepatan 60 km/h

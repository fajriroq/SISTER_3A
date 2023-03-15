import time

# waktu rata-rata dari beberapa pengukuran waktu
def calculate_average_time(time_list):
    return sum(time_list) / len(time_list)

# menjalankan algoritma Cristian tanpa server
def run_cristian_algorithm():
    # Melakukan beberapa pengukuran waktu
    time_list = []
    for i in range(20):
        start_time = int(time.time() * 500)
        time.sleep(0.1)
        end_time = int(time.time() * 500)
        time_list.append((start_time + end_time) // 2)

    # Menghitung waktu rata-rata dari beberapa pengukuran waktu
    avg_time = calculate_average_time(time_list)

    # Menampilkan waktu yang telah disesuaikan
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(avg_time / 500))
    print('Menggunakan algoritma Cristian: ', time_str)

# Menjalankan algoritma Cristian tanpa server
run_cristian_algorithm()

import time

def calculate_average_time(time_list):
    return sum(time_list) / len(time_list)

def run_berkeley_algorithm(server_time):
    current_time = int(time.time() * 1000)
    time_diff = server_time - current_time
    new_time = current_time + time_diff
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(new_time / 1000))
    print('Waktu sekarang saat disesuaikan algoritma Berkeley: ', time_str)

def run_berkeley_algorithm_without_server():
    time_list = []
    for i in range(10):
        start_time = int(time.time() * 1000)
        time.sleep(0.1)
        end_time = int(time.time() * 1000)
        time_list.append((start_time + end_time) // 2)

    avg_time = calculate_average_time(time_list)

    run_berkeley_algorithm(avg_time)

run_berkeley_algorithm_without_server()
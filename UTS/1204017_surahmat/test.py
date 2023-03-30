import os
import time

def rental_process(rental_id, customer_name):
    # Simulasi proses penyewaan
    print(f"Proses penyewaan dengan ID {rental_id} untuk {customer_name} dimulai...")
    time.sleep(3)
    print(f"Proses penyewaan dengan ID {rental_id} untuk {customer_name} selesai.")
    return rental_id

def spawn_process(func, args):

    process_id = os.getpid()
    print(f"Child process dengan ID {process_id} dimulai...")
    result = func(*args)
    print(f"Child process dengan ID {process_id} selesai. Hasil: {result}")

if __name__ == '__main__':
    # List penyewaan
    rental_list = [('R001', 'John'), ('R002', 'Jane'), ('R003', 'Doe')]


    parent_process_id = os.getpid()
    print(f"Parent process dengan ID {parent_process_id} dimulai...")


    for rental in rental_list:
        spawn_process(rental_process, rental)

    print(f"Parent process dengan ID {parent_process_id} selesai.")

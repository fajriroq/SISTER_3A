import multiprocessing
import time

def process_service(service_data):
    print(f"Memproses layanan komunitas dengan ID {service_data['id']}...")
    print(f"Nama Layanan : {service_data['title']}")


def spawn_processes(community_services):
    processes = []
    for service_data in community_services:
        process = multiprocessing.Process(target=process_service, args=(service_data,))
        processes.append(process)
    
    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    
    community_services_to_process = [
        {"id": 1, "title": "Membarsihkan Pantai"},
        {"id": 2, "title": "Menanam pohon"},
        {"id": 3, "title": "Membari Makan gelandangan"}
    ]
    start_time = time.time()
    spawn_processes(community_services_to_process)
    end_time = time.time()
    print(f"Elapsed Time: {end_time - start_time} seconds")
    print("Selesai")

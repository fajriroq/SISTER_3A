from mpi4py import MPI
import requests
import random

comm = MPI.COMM_WORLD
rank = comm.rank

url = "https://reqres.in/api/users?page=2"

if rank == 0:
    res = requests.get(url)
    users = res.json()['data']
    for user in users:
        first_name = user['first_name']
        comm.send(first_name, dest=1)
        print(f"Data {first_name} telah dikirim ke proses 1")
    
elif rank == 1:
    for i in range(5):
        first_name = comm.recv(source=0)
        gaji_pokok = 1000000
        gaji = gaji_pokok * random.uniform(0.8, 1.2)
        print(f"Gaji {first_name}: {gaji}")
else:
    print(f"Proses {rank} tidak melakukan apa-apa")
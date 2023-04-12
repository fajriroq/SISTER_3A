import http.client
import json
import time

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    activitys = []
    print("Searching for random activity...")
    for i in range(2):
        conn = http.client.HTTPSConnection("www.boredapi.com")
        conn.request("GET", "/api/activity/")
        response = conn.getresponse()
        activity_data = json.loads(response.read().decode())
        conn.close()
        activitys.append(activity_data['activity'])
        print(f"Process {rank} found activity: {activity_data['activity']}")
        print(f"Found activity: {activity_data['activity']}")
        time.sleep(2)

    for i in activitys:
        print(f"broadcast activity {i}")
        for index in range(1, comm.Get_size()):
            comm.send(i, dest=index)

else:
    count = 0
    while True:
        status = MPI.Status()
        if comm.iprobe(status=status):
            activity = comm.recv(source=0)
            print(f"Process {rank} received activity: {activity}")
            count += 1
        elif count == 2:
            break
        else:
            time.sleep(1)

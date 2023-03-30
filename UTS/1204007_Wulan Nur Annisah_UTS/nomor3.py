from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("pengajuan pembayaran SPP: " , rank)

if rank==0:
    data= 7600000
    destination_process = 4
    comm.send(data,dest=destination_process)
    print ("sending data %s " %data +\
           "to process %d" %destination_process)
   
if rank==1:
    destination_process = 8
    data= "Selamat Datang"
    comm.send(data,dest=destination_process)
    print ("Sending data %s :" %data + \
           "to process %d" %destination_process)

if rank==2:
    destination_process = 12
    data= "Pembayaran Diterima"
    comm.send(data,dest=destination_process)
    print ("Sending data %s :" %data + \
           "to process %d" %destination_process)   

if rank==4:
    data=comm.recv(source=0)
    print ("Pengajuan diterima = %s" %data)
    
    
if rank==12:
    data1=comm.recv(source=2)
    print ("Pembayaran Selesai = %s" %data1)

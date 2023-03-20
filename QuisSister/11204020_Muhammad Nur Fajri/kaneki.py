import time
import os
from random import randint
from threading import Thread, Barrier

class ProgramInput (Thread):
   def __init__(self, name, duration, barrier):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.nilai = ["statik","multimedia","jaringan"]
      self.data = []
      self.jumlah = len(self.nilai)
      self.barrier = barrier

   def run(self):
      start_time = time.time()
      print ("---> " + self.name + \
               " running, belonging to process ID "\
               + str(os.getpid() +self.duration) + "\n")
      
      for i in range(len(self.nilai)):
         nilaiMhs = input("mata kuliah "+self.nilai[i] +" di tetapkan di hari : ")
         self.data.append(self.nilai[i] + "      " + nilaiMhs)
      
      self.barrier.wait()
      if len(self.data) > 0:
         print("")
         print("Mohon Di Tunggu untuk hasil resultnya ya...")
         print("")
         print("==== Mata Kuliah ==== Hari ====")
         for i in self.data:
            time.sleep(self.duration)
            print("     "+i)
      else:
         print("nilai tidak di isi")

      print("waktu yang di habiskan dalam 1 program--- %s seconds ---" % (time.time() - start_time))


def main():
    
    num_threads = 1
    barrier = Barrier(num_threads+1)
  
    Prog = ProgramInput("Input Nilai", randint(1,10), barrier)
    
    Prog.start()
    
    barrier.wait()
    
   
if __name__ == "__main__":
  
    local_time = time.time()
    print("program mulai berjalan:", time.ctime(local_time))  
    main()


import threading 
import time

class Employee(threading.Thread):
    def __init__(self, name, barrier):
        threading.Thread.__init__(self)
        self.name = name
        self.barrier = barrier

def hitung_rata_rata(nilai):
    total = 0
    for n in nilai:
        total += n
    rata_rata = total / len(nilai)
    return rata_rata


nilai_mhs = [80, 85, 90, 95, 75, 100]
rata_rata_mhs = hitung_rata_rata(nilai_mhs)

def main():
    num_of_employees = 10
    barrier = threading.Barrier(num_of_employees)
    employees = []
    for i in range(num_of_employees):
        employee = Employee("Dosen-" + str(i+1), barrier)
        employees.append(employee)

    for employee in employees:
        employee.start()

    for employee in employees:
        employee.join()

    print("Rata-rata nilai mahasiswa: ", rata_rata_mhs)

def hitung_rata_nilai(nilai):
    jumlah = sum(nilai)
    rata_rata = jumlah / len(nilai)
    return rata_rata

nama = input("Masukkan nama mahasiswa: ")
nilai = []

while True:
    nilai_str = input("Masukkan nilai (atau ketik 'selesai' jika sudah selesai): ")
    if nilai_str == 'selesai':
        break
    nilai.append(float(nilai_str))

rata_rata = hitung_rata_nilai(nilai)

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 60:
    grade = "C"
elif nilai_akhir >= 50:
    grade = "D"
else:
    grade = "E"

print(f"Mahasiswa dengan nama {nama} mendapatkan nilai akhir {nilai_akhir:.2f} dan mendapat grade {grade}")


if __name__ == "__main__":
    main()
# main.py
from tasks import add_numbers

result = add_numbers.delay(5, 10)  # Menjalankan tugas secara asinkronus
print("menjalankan task!!")
print(f"Task ID: {result.id}")

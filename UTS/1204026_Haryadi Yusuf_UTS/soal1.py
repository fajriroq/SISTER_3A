import multiprocessing
import time

def create_schedule(course_name, course_schedule):
    
    print(f"Jadwal Kuliah untuk {course_name}:")
    for day, schedule in course_schedule.items():
        print(f"{day}: {schedule}")
    time.sleep(2) 

if __name__ == '__main__':
    course_a_schedule = {
        "Senin": "10.00 - 12.00",
        "Selasa": "13.00 - 15.00",
        "Rabu": "8.00 - 10.00"
    }
    course_b_schedule = {
        "Kamis": "9.00 - 11.00",
        "Jumat": "14.00 - 16.00",
        "Sabtu": "10.00 - 12.00"
    }
    course_c_schedule = {
        "Senin": "8.00 - 10.00",
        "Kamis": "14.00 - 16.00",
        "Jumat": "10.00 - 12.00"
    }
    course_d_schedule = {
        "Selasa": "9.00 - 11.00",
        "Rabu": "13.00 - 15.00",
        "Sabtu": "8.00 - 10.00"
    }   
    courses = [("Kursus Sistem Tersebar", course_a_schedule), 
               ("Kursus AI", course_b_schedule), 
               ("Kursus Sitem Multimedia", course_c_schedule), 
               ("Kursus Statitistika", course_d_schedule)]
    processes = []
    for course in courses:
        p = multiprocessing.Process(target=create_schedule, args=course)
        processes.append(p)
        p.start()  
    for p in processes:
        p.join()
    print("Selesai membuat jadwal kuliah untuk semua kursus.")

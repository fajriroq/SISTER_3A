import multiprocessing
import time

def book_concert_ticket(concert_name, ticket_info):
    print(f"Pemesanan tiket untuk konser {concert_name}:")
    print(f"Informasi tiket: {ticket_info}")
    time.sleep(2)

if __name__ == '__main__':
    concert_a_info = {
        "Tanggal": "1 Januari 2024",
        "Waktu": "19.00 WIB",
        "Tempat": "Gelora Bung Karno",
        "Kategori": "VIP"
    }
    concert_b_info = {
        "Tanggal": "15 Februari 2024",
        "Waktu": "20.00 WIB",
        "Tempat": "Istora Senayan",
        "Kategori": "Festival"
    }
    concert_c_info = {
        "Tanggal": "10 Maret 2024",
        "Waktu": "18.30 WIB",
        "Tempat": "JIEXPO Kemayoran",
        "Kategori": "Tribune"
    }
    concert_d_info = {
        "Tanggal": "5 April 2024",
        "Waktu": "19.30 WIB",
        "Tempat": "ICE BSD",
        "Kategori": "Regular"
    }
    concerts = [
        ("Konser A", concert_a_info),
        ("Konser B", concert_b_info),
        ("Konser C", concert_c_info),
        ("Konser D", concert_d_info)
    ]
    processes = []
    for concert in concerts:
        p = multiprocessing.Process(target=book_concert_ticket, args=concert)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("Pemesanan tiket konser selesai untuk semua konser.")

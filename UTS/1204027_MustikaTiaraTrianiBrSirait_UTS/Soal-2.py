import multiprocessing
import time

# Fungsi untuk memproses pesanan makanan
def process_order(restaurant_name, customer_name, menu, target=None):
    print("Memproses pesanan dari", customer_name, "di", restaurant_name)
    for item in menu:
        if target is None or item.lower().startswith(target.lower()):
            print("Membuat", item)
            time.sleep(1)  # Delay 1 detik setiap pembuatan menu
    print("Pesanan dari", customer_name, "telah selesai")

if __name__ == "__main__":
    # Daftar pesanan dari pelanggan
    orders = [
        {"restoran": "Pizza Hut", "pelanggan": "John Doe", "menu": ["Pepperoni Pizza", "Garlic Bread", "Coke"]},
        {"restoran": "Burger King", "pelanggan": "Jane Doe", "menu": ["Whopper", "French Fries", "Sprite"]},
        {"restoran": "KFC", "pelanggan": "Jack Smith", "menu": ["Fried Chicken", "Mashed Potato", "Pepsi"]},
    ]

    # Membuat proses untuk memproses setiap pesanan dengan jenis makanan tertentu
    target = "Pizza"
    processes = []
    for order in orders:
        p = multiprocessing.Process(target=process_order, args=(order["restoran"], order["pelanggan"], order["menu"], target))
        processes.append(p)

    # Memulai semua proses pemrosesan pesanan secara bersama-sama
    for p in processes:
        p.start()

    # Menunggu semua proses selesai
    for p in processes:
        p.join()
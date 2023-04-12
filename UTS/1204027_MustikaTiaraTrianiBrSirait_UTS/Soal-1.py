import multiprocessing

def process_order(restaurant_name, customer_name, menu):
    print("Memproses pesanan dari", customer_name, "di", restaurant_name)
    for item in menu:
        print("Membuat", item)
    print("Pesanan dari", customer_name, "telah selesai")

if __name__ == "__main__":

    order = {"restoran": "Pizza Hut", "pelanggan": "Dira", "menu": ["BigBox", "Double Meal", "Splitza"]}

    p = multiprocessing.Process(target=process_order, args=(order["restoran"], order["pelanggan"], order["menu"]))

    p.start()

    p.join()

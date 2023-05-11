import asyncio


@asyncio.coroutine
def take_order(menu_item):
    """
    Coroutine untuk mengambil pesanan dari pelanggan.
    """
    print(f"Taking order for {menu_item}...")
    yield from asyncio.sleep(2)  # simulasi waktu untuk mengambil pesanan
    print(f"Order for {menu_item} taken.")


@asyncio.coroutine
def prepare_food(menu_item):
    """
    Coroutine untuk mempersiapkan makanan yang dipesan.
    """
    print(f"Preparing {menu_item}...")
    yield from asyncio.sleep(5)  # simulasi waktu untuk mempersiapkan makanan
    print(f"{menu_item} prepared.")


@asyncio.coroutine
def serve_food(table_number, menu_item):
    """
    Coroutine untuk menyajikan makanan ke pelanggan.
    """
    print(f"Serving {menu_item} to table {table_number}...")
    yield from asyncio.sleep(3)  # simulasi waktu untuk menyajikan makanan
    print(f"{menu_item} served to table {table_number}.")


if __name__ == '__main__':
    # Membuat event loop
    loop = asyncio.get_event_loop()

    # Menjalankan coroutine secara bersamaan
    tasks = [
        take_order('Pasta'),
        prepare_food('Pasta'),
        serve_food(1, 'Pasta'),
        take_order('Steak'),
        prepare_food('Steak'),
        serve_food(2, 'Steak'),
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    # Menutup event loop
    loop.close()

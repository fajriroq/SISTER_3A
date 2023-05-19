import asyncio
import random

async def greet_customer(table_number):
    print(f"Karyawan: Selamat datang di restoran kami. Silakan duduk di meja {table_number}.")
    await asyncio.sleep(random.randint(1, 5))

async def take_order(table_number):
    print(f"Karyawan: Apa yang ingin Anda pesan di meja {table_number}?")
    await asyncio.sleep(random.randint(1, 5))

async def prepare_food(table_number):
    print(f"Karyawan: Segera kami siapkan pesanan Anda di meja {table_number}.")
    await asyncio.sleep(random.randint(1, 5))

async def serve_food(table_number):
    print(f"Karyawan: Inilah pesanan Anda di meja {table_number}. Selamat menikmati!")
    await asyncio.sleep(random.randint(1, 5))

async def clear_table(table_number):
    print(f"Karyawan: Silakan tinggalkan meja {table_number}. Terima kasih telah datang ke restoran kami.")
    await asyncio.sleep(random.randint(1, 5))

async def restaurant_flow(table_number):
    await greet_customer(table_number)
    await take_order(table_number)
    await prepare_food(table_number)
    await serve_food(table_number)
    await clear_table(table_number)

if __name__ == '__main__':
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.ensure_future(restaurant_flow(i)))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

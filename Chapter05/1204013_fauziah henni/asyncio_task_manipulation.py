import asyncio
import random

async def take_order(table_number):
    print(f"Table {table_number}: Taking order...")
    await asyncio.sleep(random.randint(1, 5))

async def prepare_food(table_number):
    print(f"Table {table_number}: Preparing food...")
    await asyncio.sleep(random.randint(1, 5))

async def serve_food(table_number):
    print(f"Table {table_number}: Serving food...")
    await asyncio.sleep(random.randint(1, 5))

async def clear_table(table_number):
    print(f"Table {table_number}: Clearing table...")
    await asyncio.sleep(random.randint(1, 5))

async def restaurant_flow(table_number):
    await take_order(table_number)
    await prepare_food(table_number)
    await serve_food(table_number)
    await clear_table(table_number)
    print(f"Table {table_number}: Done.")

if __name__ == '__main__':
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.ensure_future(restaurant_flow(i)))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

import asyncio
import random

async def take_order(customer_name, order_id):
    print(f"Taking order {order_id} for {customer_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished taking order {order_id} for {customer_name}")

async def prepare_food(order_id):
    print(f"Preparing food for order {order_id}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished preparing food for order {order_id}")

async def serve_food(order_id, customer_name):
    print(f"Serving food for order {order_id} to {customer_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished serving food for order {order_id} to {customer_name}")

async def clean_table(table_number):
    print(f"Cleaning table {table_number}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished cleaning table {table_number}")

async def waiter(name, num_tables):
    print(f"{name} started working")
    table_numbers = list(range(1, num_tables+1))
    while True:
        if len(table_numbers) == 0:
            break
        table_number = table_numbers.pop()
        await take_order(f"Customer at table {table_number}", table_number)
        await prepare_food(table_number)
        await serve_food(table_number, f"Customer at table {table_number}")
        await clean_table(table_number)
    print(f"{name} finished working")

async def restaurant(num_waiters, num_tables):
    print("Restaurant is open")
    await asyncio.gather(*(waiter(f"Waiter {i}", num_tables) for i in range(num_waiters)))
    print("Restaurant is closed")

if __name__ == '__main__':
    random.seed(42)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(restaurant(2, 5))
    loop.close()

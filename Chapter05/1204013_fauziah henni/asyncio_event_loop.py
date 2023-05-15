import asyncio
import time
import random

async def take_order(customer_name):
    print(f"Taking order for {customer_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished taking order for {customer_name}")

async def prepare_food(order_id):
    print(f"Preparing food for order {order_id}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished preparing food for order {order_id}")

async def serve_food(order_id, customer_name):
    print(f"Serving food for order {order_id} to {customer_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished serving food for order {order_id} to {customer_name}")

async def customer(name):
    print(f"Customer {name} arrived at the restaurant")
    await asyncio.gather(take_order(name), prepare_food(name), serve_food(name, name))
    print(f"Customer {name} finished dining")

async def restaurant(num_customers):
    print("Restaurant is open")
    await asyncio.gather(*(customer(f"Customer {i}") for i in range(num_customers)))
    print("Restaurant is closed")

if __name__ == '__main__':
    random.seed(42)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(restaurant(5))
    loop.close()

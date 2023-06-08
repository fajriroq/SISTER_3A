import asyncio


async def process_item(item):
    # Simulasi pemrosesan item
    await asyncio.sleep(1)
    print(f"Item {item} diproses")


async def communicate_with_warehouse(item):
    # Simulasi komunikasi dengan sistem gudang
    await asyncio.sleep(0.5)
    print(f"Item {item} dikirim ke sistem gudang")


async def warehouse_system(item):
    await communicate_with_warehouse(item)
    await process_item(item)


async def main():
    items = [1, 2, 3, 4, 5]
    tasks = []

    for item in items:
        task = asyncio.create_task(warehouse_system(item))
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())

import asyncio


async def book_ticket(concert):
    # Simulate ticket booking process
    for _ in range(10000000):
        pass
    return concert


async def evaluate(concert):
    result_concert = await book_ticket(concert)
    print('Ticket booked for concert:', result_concert)


async def main():
    concerts = [
        ["Artist 1 Concert", "2023-07-01", "A1"],
        ["Artist 2 Concert", "2023-07-02", "B2"],
        ["Artist 3 Concert", "2023-07-03", "C3"],
    ]
    tasks = []

    for concert in concerts:
        task = asyncio.create_task(evaluate(concert))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

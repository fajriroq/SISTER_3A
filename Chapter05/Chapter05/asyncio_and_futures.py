import asyncio
import sys


async def first_coroutine(future: asyncio.Future, num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    future.set_result('First coroutine (sum of N ints) result = %s' % count)


async def second_coroutine(future: asyncio.Future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    future.set_result('Second coroutine (factorial) result = %s' % count)


def got_result(future: asyncio.Future):
    print(future.result())


async def main():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"arg 1 : {num1}")
    print(f"arg 2 : {num2}")

    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    tasks = [loop.create_task(first_coroutine(future1, num1)), loop.create_task(second_coroutine(future2, num2))]

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
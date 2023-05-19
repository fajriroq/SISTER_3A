import asyncio
import time
import random

def coba_1(end_time, loop):
    print ("coba_1 called")
    time.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, coba_2, end_time, loop)
    else:
        loop.stop()

def coba_2(end_time, loop):
    print ("coba_2 called ")
    time.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, coba_3, end_time, loop)
    else:
        loop.stop()

def coba_3(end_time, loop):
    print ("coba_3 called")
    time.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, coba_1, end_time, loop)
    else:
        loop.stop()


async def main():
    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 20
    loop.call_soon(coba_1, end_loop, loop)

asyncio.run(main())

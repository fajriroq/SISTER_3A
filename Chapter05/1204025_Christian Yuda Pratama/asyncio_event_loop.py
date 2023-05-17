import asyncio
import random

async def task_A(end_time, loop):
    print("task_A called")
    await asyncio.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.create_task, task_B(end_time, loop))
    else:
        loop.stop()

async def task_B(end_time, loop):
    print("task_B called")
    await asyncio.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.create_task, task_C(end_time, loop))
    else:
        loop.stop()

async def task_C(end_time, loop):
    print("task_C called")
    await asyncio.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.create_task, task_A(end_time, loop))
    else:
        loop.stop()

loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(asyncio.create_task, task_A(end_loop, loop))
loop.run_forever()

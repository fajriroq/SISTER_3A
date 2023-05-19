import asyncio


@asyncio.coroutine
def clock_in(name):
    """
    Coroutine untuk melakukan check-in pegawai.
    """
    print(f"{name} clocked in.")


@asyncio.coroutine
def do_work(name, task):
    """
    Coroutine untuk melakukan tugas pekerjaan.
    """
    print(f"{name} is working on {task}...")
    yield from asyncio.sleep(5)  # simulasi waktu untuk menyelesaikan tugas
    print(f"{name} completed {task}.")


@asyncio.coroutine
def clock_out(name):
    """
    Coroutine untuk melakukan check-out pegawai.
    """
    print(f"{name} clocked out.")


if __name__ == '__main__':
    # Membuat event loop
    loop = asyncio.get_event_loop()

    # Menjalankan coroutine secara bersamaan
    tasks = [
        clock_in('Alice'),
        do_work('Alice', 'report'),
        do_work('Alice', 'presentation'),
        clock_out('Alice'),
        clock_in('Bob'),
        do_work('Bob', 'coding'),
        do_work('Bob', 'testing'),
        clock_out('Bob'),
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    # Menutup event loop
    loop.close()

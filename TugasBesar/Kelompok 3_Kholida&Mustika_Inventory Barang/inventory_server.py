import asyncio
import Pyro4
from mpi4py import MPI
from multiprocessing import Barrier

@Pyro4.expose
class Inventory:
    def __init__(self, barrier):
        self.inventory = {}
        self.barrier = barrier

    def add_item(self, item_id, item_name):
        if item_id in self.inventory:
            return "Item sudah tersedia"
        self.inventory[item_id] = item_name
        return "Item berhasil ditambahkan"

    def remove_item(self, item_id):
        if item_id not in self.inventory:
            return "Item tidak ditemukan"
        del self.inventory[item_id]
        return "Item berhasil dihapus"

    def update_item(self, item_id, new_name):
        if item_id not in self.inventory:
            return "Item tidak ditemukan"
        self.inventory[item_id] = new_name
        return "Item berhasil diupdate"

    def get_all_items(self):
        return self.inventory

    def get_item_details(self, item_id):
        if item_id not in self.inventory:
            return "Item tidak ditemukan"
        return self.inventory[item_id]

async def serve_inventory(barrier):
    inventory = Inventory(barrier)
    daemon = Pyro4.Daemon()
    uri = daemon.register(inventory)
    print("Server URI:", uri)

    with Pyro4.locateNS() as ns:
        ns.register("inventory", uri)

    print("Server is ready.")

    async def start_daemon():
        await asyncio.get_event_loop().run_in_executor(None, daemon.requestLoop)

    await asyncio.gather(start_daemon())

def do_something():
    print("Doing something")

async def myFunc():
    print("Running myFunc")

async def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    barrier = Barrier(size)

    if rank == 0:
        await serve_inventory(barrier)
    else:
        do_something()
        barrier.wait()
        await myFunc()

    barrier.wait()
    await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())

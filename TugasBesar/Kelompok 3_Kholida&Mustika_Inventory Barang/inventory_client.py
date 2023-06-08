import asyncio
import Pyro4
from mpi4py import MPI

async def connect_to_server():
    inventory = Pyro4.Proxy("PYRONAME:inventory")

    while True:
        print("\n=== Menu Program Pengelolaan Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Update Barang")
        print("4. Tampilkan Semua Barang")
        print("5. Tampilkan Detail Barang")
        print("0. Keluar")

        choice = input("Masukkan Pilihan Anda: ")

        if choice == "1":
            item_id = input("Masukkan item ID: ")
            item_name = input("Masukkan Nama item: ")
            result = inventory.add_item(item_id, item_name)
            print(result)

        elif choice == "2":
            item_id = input("Masukkan item ID Untuk Menghapus: ")
            result = inventory.remove_item(item_id)
            print(result)

        elif choice == "3":
            item_id = input("Masukkan item ID Untuk update: ")
            new_name = input("Masukkan Nama Item Barue: ")
            result = inventory.update_item(item_id, new_name)
            print(result)

        elif choice == "4":
            items = inventory.get_all_items()
            if items:
                print("=== Semua Items ===")
                for item_id, item_name in items.items():
                    print(f"ID: {item_id}, Nama: {item_name}")
            else:
                print("Barang Tidak Ditemukan.")

        elif choice == "5":
            item_id = input("Masukkan item ID Untuk Menampilkan Detail : ")
            item_name = inventory.get_item_details(item_id)
            if item_name:
                print("=== Item Details ===")
                print(f"ID: {item_id}, Nama: {item_name}")
            else:
                print("Item Tidak Ditemukan.")

        elif choice == "0":
            break

        else:
            print("Invalid Pilihan. Mohon Coba Lagi.")

async def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    if rank == 0:
        await connect_to_server()

    barrier = comm.bcast(None, root=0)
    await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())

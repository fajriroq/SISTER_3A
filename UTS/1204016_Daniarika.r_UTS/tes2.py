import multiprocessing
import time


def update_stock(drug_name):
    print(
        f"Proses {multiprocessing.current_process().name} sedang memperbarui stok obat {drug_name}...")

    # Melakukan simulasi waktu pemrosesan
    time.sleep(1)

    print(
        f"Proses {multiprocessing.current_process().name} selesai memperbarui stok obat {drug_name}.")


if __name__ == '__main__':
    drugs = ['Paracetamol', 'Ibuprofen', 'Aspirin']

    for drug in drugs:
        process = multiprocessing.Process(target=update_stock, args=(drug,))
        process.start()
        process.join()

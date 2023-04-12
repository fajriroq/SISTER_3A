import multiprocessing


def register_participant(nama, umur, alamat, lomba, email):
    import time
    time.sleep(3)

    print('\nSTATUS :\n')

    print(f"{nama} berhasil terdaftar untuk lomba kemerdekaan")

if __name__ == '__main__':
    print('\nSilahkan Mendaftar Terlebih Dahulu !!!\n')
    nama = input("Masukkan nama peserta: ")
    umur = int(input("Masukkan umur peserta: "))
    alamat = input("Masukkan alamat peserta: ")
    lomba = input("Jenis Lomba yang akan diikuti : ")
    email = input("Masukkan Alamat Email Peserta : ")

    p = multiprocessing.Process(target=register_participant, args=(nama, umur, alamat, lomba, email))

    p.start()
    p.join()

    print("\nProses pendaftaran selesai\n")

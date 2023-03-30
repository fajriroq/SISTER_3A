import multiprocessing

def spawn(airline, passenger, destination):
    print(f"{passenger} telah memesan tiket penerbangan dengan {airline} ke {destination}")

if __name__ == '__main__':
    # Daftar pemesanan tiket penerbangan
    flight_bookings = [('Garuda Indonesia', 'John Doe', 'Bali'),
                       ('Lion Air', 'Jane Doe', 'Jakarta'),
                       ('Citilink', 'James Bond', 'Surabaya')]

    # Parent process
    for booking in flight_bookings:
        airline, passenger, destination = booking
        p = multiprocessing.Process(target=spawn, args=(airline, passenger, destination))
        p.start()
        p.join()

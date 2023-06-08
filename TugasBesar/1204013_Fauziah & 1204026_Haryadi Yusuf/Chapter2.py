from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_tickets = 4
booking_barrier = Barrier(num_tickets)
concerts = ['Concert 1', 'Concert 2', 'Concert 3', 'Concert 4']

def book_ticket():
    concert = concerts.pop()
    sleep(randrange(2, 5))
    print('%s booked a ticket at: %s\n' % (concert, ctime()))
    booking_barrier.wait()

def main():
    threads = []
    print('Ticket Booking Started!')
    for _ in range(num_tickets):
        threads.append(Thread(target=book_ticket))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Ticket Booking Completed!')

if __name__ == "__main__":
    main()

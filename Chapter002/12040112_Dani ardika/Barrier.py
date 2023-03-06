from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()


def main():
    threads = []
    choice = input("balapan kah bree kalau mau koo, tulis ma ki (y) klo tidak tulis ko (n))? (y/n): ")
    if choice == 'y':
        print('START RACE!!!!')
        for i in range(num_runners):
            threads.append(Thread(target=runner))
            threads[-1].start()

        for thread in threads:
            thread.join()
            print('Race over!')
    elif choice == 'n':
        print('Race cancelled!')
    else:
        print('Invalid input! Please try again.')


if __name__ == "__main__":
    main()

    

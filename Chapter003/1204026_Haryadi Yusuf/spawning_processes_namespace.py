import multiprocessing
from myFunc import simple_looping

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=simple_looping, args=(i,))
        process.start()
        process.join()


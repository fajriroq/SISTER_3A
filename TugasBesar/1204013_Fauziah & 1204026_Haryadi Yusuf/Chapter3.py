import multiprocessing
import time


def book_ticket(concert):
    # Simulate ticket booking process
    for _ in range(10000000):
        pass
    return concert


def evaluate(concert):
    result_concert = book_ticket(concert)
    print('Ticket booked for concert:', result_concert)


if __name__ == '__main__':
    concerts = [
        ["Artist 1 Concert", "2023-07-01", "A1"],
        ["Artist 2 Concert", "2023-07-02", "B2"],
        ["Artist 3 Concert", "2023-07-03", "C3"],
    ]
    processes = []

    start_time = time.perf_counter()

    for concert in concerts:
        process = multiprocessing.Process(target=evaluate, args=(concert,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print('Execution time:', end_time - start_time)

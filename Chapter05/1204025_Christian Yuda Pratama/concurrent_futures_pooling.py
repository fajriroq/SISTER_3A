import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number


def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))


if __name__ == '__main__':
    # Sequential Execution
    start_time = time.process_time()
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.process_time() - start_time))

    # Thread Pool Execution
    start_time = time.process_time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(evaluate, number_list)
    print('Thread Pool Execution in %s seconds' % (time.process_time() - start_time))

    # Process Pool Execution
    start_time = time.process_time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(evaluate, number_list)
    print('Process Pool Execution in %s seconds' % (time.process_time() - start_time))

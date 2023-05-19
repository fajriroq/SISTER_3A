import concurrent.futures
import time

employees = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def work(name, task):
    print(f'{name} is starting task: {task}')
    for i in range(0, 10000000):
        i += 1
    print(f'{name} finished task: {task}')

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for employee in employees:
        work(employee, 'data entry')
        work(employee, 'customer service')
    print(f'Sequential Execution in {time.perf_counter() - start_time} seconds')

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        tasks = []
        for employee in employees:
            tasks.append(executor.submit(work, employee, 'data entry'))
            tasks.append(executor.submit(work, employee, 'customer service'))
        for task in concurrent.futures.as_completed(tasks):
            task.result()
    print(f'Thread Pool Execution in {time.perf_counter() - start_time} seconds')

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        tasks = []
        for employee in employees:
            tasks.append(executor.submit(work, employee, 'data entry'))
            tasks.append(executor.submit(work, employee, 'customer service'))
        for task in concurrent.futures.as_completed(tasks):
            task.result()
    print(f'Process Pool Execution in {time.perf_counter() - start_time} seconds')

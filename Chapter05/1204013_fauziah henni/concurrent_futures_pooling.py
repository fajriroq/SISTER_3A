import concurrent.futures
import time

menu = {
    'nasi goreng': 15000,
    'mie goreng': 12000,
    'ayam goreng': 20000,
    'sate ayam': 15000,
    'gado-gado': 10000,
    'bakso': 12000,
    'es teh manis': 5000,
    'es jeruk': 7000,
    'jus alpukat': 10000,
    'jus mangga': 12000
}

order_list = [
    ('nasi goreng', 2),
    ('ayam goreng', 1),
    ('es teh manis', 3),
    ('jus mangga', 1)
]


def prepare_food(item, quantity):
    for i in range(0, 10000000):
        i += 1
    print(f'Prepared {quantity} {item}(s)')


def serve_customer(item, quantity):
    for i in range(0, 10000000):
        i += 1
    print(f'Served {quantity} {item}(s)')


def take_order(order):
    item, quantity = order
    price = menu[item]
    print(f'Taking order: {quantity} {item}(s), price {price*quantity}')
    return price*quantity


if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    total_price = 0
    for order in order_list:
        price = take_order(order)
        total_price += price
        prepare_food(*order)
        serve_customer(*order)
    print(f'Sequential Execution in {time.perf_counter() - start_time} seconds, total price: {total_price}')

    # Thread Pool Execution
    start_time = time.perf_counter()
    total_price = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for order in order_list:
            futures.append(executor.submit(take_order, order))
        for future in concurrent.futures.as_completed(futures):
            price = future.result()
            total_price += price
        for order in order_list:
            executor.submit(prepare_food, *order)
            executor.submit(serve_customer, *order)
    print(f'Thread Pool Execution in {time.perf_counter() - start_time} seconds, total price: {total_price}')

    # Process Pool Execution
    start_time = time.perf_counter()
    total_price = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = []
        for order in order_list:
            futures.append(executor.submit(take_order, order))
        for future in concurrent.futures.as_completed(futures):
            price = future.result()
            total_price += price
        for order in order_list:
            executor.submit(prepare_food, *order)
            executor.submit(serve_customer, *order)
    print(f'Process Pool Execution in {time.perf_counter() - start_time} seconds, total price: {total_price}')

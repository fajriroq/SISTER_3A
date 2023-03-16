import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

MAX_CAPACITY = 20
MIN_CAPACITY = 5

items = []
condition = threading.Condition()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:
            while len(items) == 0:
                logging.info('No items to consume. Waiting...')
                condition.wait()

            item = items.pop(0)
            logging.info('Consumed 1 item: %s', item)

            condition.notify()

    def run(self):
        while True:
            time.sleep(2)
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:
            while len(items) >= MAX_CAPACITY:
                logging.info(
                    'Items produced: %s. Max capacity reached. Waiting...', len(items))
                condition.wait()

            item = 'item-' + str(time.time())
            items.append(item)
            logging.info('Produced 1 item: %s. Total items: %s',
                         item, len(items))

            condition.notify()

    def run(self):
        while True:
            time.sleep(1)
            self.produce()


class StockManager(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_stock(self):
        with condition:
            if len(items) < MIN_CAPACITY:
                logging.info('Low stock: %s. Restocking...', len(items))

                for i in range(MIN_CAPACITY - len(items)):
                    item = 'item-' + str(time.time())
                    items.append(item)

                logging.info('Restocked. Total items: %s', len(items))

    def run(self):
        while True:
            time.sleep(5)
            self.check_stock()


def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')
    stock_manager = StockManager(name='StockManager')

    producer.start()
    consumer.start()
    stock_manager.start()

    producer.join()
    consumer.join()
    stock_manager.join()


if __name__ == "__main__":
    main()

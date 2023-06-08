import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class pembeli1(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pengunjung(self):

        with condition:

            if len(items) == 0:
                logging.info('PRODUK HABIS!!')
                condition.wait()

            items.pop()
            logging.info('Mendapat produk')

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(2)
            self.pengunjung()


class sales1(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pengelola(self):

        with condition:

            if len(items) == 5:
                logging.info('Produk Elekrtonik Tersisa {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('Produk Elektronik {} Tersedia'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.5)
            self.pengelola()


def main():
    sales = sales1(name='Sales')
    pembeli = pembeli1(name='Pembeli')

    sales.start()
    pembeli.start()

    sales.join()
    pembeli.join()


if __name__ == "__main__":
    main()

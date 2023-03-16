import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting thread ", self.name)
        time.sleep(2)
        print("Ending thread ", self.name)


def main():
    threads = []
    for i in range(5):
        thread = MyThread(str(i))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()

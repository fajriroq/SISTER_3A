import random
import threading


class MonteCarloPi(threading.Thread):
    def __init__(self, iterations):
        threading.Thread.__init__(self)
        self.iterations = iterations
        self.in_circle = 0

    def run(self):
        for i in range(self.iterations):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                self.in_circle += 1

    def get_estimate(self):
        return 4 * self.in_circle / float(self.iterations)


def main():
    n_threads = 4
    n_iterations = 1000000

    threads = []
    for i in range(n_threads):
        thread = MonteCarloPi(n_iterations // n_threads)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_in_circle = sum(thread.in_circle for thread in threads)
    total_iterations = sum(thread.iterations for thread in threads)

    pi_estimate = 4 * total_in_circle / float(total_iterations)
    print("Estimated value of pi:", pi_estimate)


if __name__ == '__main__':
    main()

import http.client
import json
import multiprocessing as mp
import random
import time


def get_random_fact():
    conn = http.client.HTTPSConnection("uselessfacts.jsph.pl")
    conn.request("GET", "/api/v2/facts/random?language=en")
    res = conn.getresponse()

    if res.status != 200:
        return ""

    data = res.read().decode("utf-8")
    print(f"Fact: {json.loads(data)['text']}")


def generate_random_fact() -> mp.Process:
    time.sleep(random.randint(1, 3))
    return mp.Process(target=get_random_fact)

def start_process(list_proc: list[mp.Process]):
    list_proc.reverse()
    for i in list_proc:
        i.start()
        time.sleep(random.randint(1, 4))

    list_proc.reverse()
    for i in list_proc:
        i.join()

if __name__ == "__main__":
    proccesses = [generate_random_fact() for i in range(3)]
    start_process(proccesses)


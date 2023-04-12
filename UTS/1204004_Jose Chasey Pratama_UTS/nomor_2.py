import http.client
import json
import multiprocessing as mp
import random
import time


def get_random_fact(queue_: mp.Queue):
    conn = http.client.HTTPSConnection("uselessfacts.jsph.pl")
    conn.request("GET", "/api/v2/facts/random?language=en")
    res = conn.getresponse()

    if res.status != 200:
        return

    data = res.read().decode("utf-8")
    json_data = json.loads(data)
    queue_.put(json_data['text'])
    return


def generate_random_fact(queue_: mp.Queue) -> mp.Process:
    print("Generating Process for random fact....")
    return mp.Process(target=get_random_fact, args=(queue_,))


def show_random_fact_mp(list_text: list[str]) -> list[mp.Process]:
    list_proc = []
    print("Generating Process using list fact..........")
    while list_text:
        random_item = random.choice(list_text)
        list_text.remove(random_item)
        list_proc.append(mp.Process(target=print, args=(f"Fact: {random_item}",)))

    return list_proc


def start_process(list_proc: list[mp.Process], delaysecs: int):
    list_proc.reverse()
    for i in list_proc:
        i.start()
        time.sleep(random.randint(0, delaysecs))

    list_proc.reverse()
    for i in list_proc:
        i.join()


if __name__ == "__main__":
    globaldata = []
    queue = mp.Queue()
    proccesses = [generate_random_fact(queue) for i in range(3)]

    start_process(proccesses, 4)

    while not queue.empty():
        globaldata.append(queue.get())

    start_process(show_random_fact_mp(globaldata), 0)

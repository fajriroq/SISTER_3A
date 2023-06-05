# tasks.py
from celery import Celery
url2="amqp://guest:guest@127.0.0.1//"

app = Celery('tasks', broker={url2})

@app.task
def add_numbers(x, y):
    result = x + y
    return result

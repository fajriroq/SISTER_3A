from celery import Celery

app = Celery('addTask', broker='amqp://guest@localhost//')


@app.task
def multiply(x: int, y: int):
    return x - y

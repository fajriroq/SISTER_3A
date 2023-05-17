from celery import Celery

app = Celery('my_project', broker='amqp://guest:**@localhost:5672//')

@app.task
def add(x, y):
    return x + y
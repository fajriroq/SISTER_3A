import asyncio
import time
from random import randint


@asyncio.coroutine
def start_state():
    print('Start Room called\n')
    input_value = randint(0, 1)
    time.sleep(1)

    if input_value == 0:
        result = yield from state2(input_value)
    else:
        result = yield from state1(input_value)

    print('Resume of the Transition : \nStart Room calling ' + result)


@asyncio.coroutine
def state1(transition_value):
    output_value = 'Room 1 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = yield from state3(input_value)
    else:
        result = yield from state2(input_value)

    return output_value + 'Room 1 calling %s' % result


@asyncio.coroutine
def state2(transition_value):
    output_value = 'Room 2 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from state3(input_value)

    return output_value + 'Room 2 calling %s' % result


@asyncio.coroutine
def state3(transition_value):
    output_value = 'Room 3 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from end_state(input_value)

    return output_value + 'Room 3 calling %s' % result


@asyncio.coroutine
def end_state(transition_value):
    output_value = 'End Room with transition value = %s\n' % transition_value
    print('...stop computation...')
    return output_value


if __name__ == '__main__':
    print('Finite Room Machine simulation with Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())

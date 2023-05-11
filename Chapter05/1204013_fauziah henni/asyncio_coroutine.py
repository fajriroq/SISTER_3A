import asyncio
import time
from random import randint


@asyncio.coroutine
def start_state():
    print('Welcome to our restaurant!')
    input_value = yield from get_input('Do you have a reservation? (y/n) ')

    if input_value.lower() == 'y':
        result = yield from reserved_state()
    else:
        result = yield from walkin_state()

    print('Resume of the Transition: \nStart State calling ' + result)


@asyncio.coroutine
def reserved_state():
    print('Great! Please give me your name and reservation number.')
    name = yield from get_input('Name: ')
    reservation_number = yield from get_input('Reservation Number: ')
    time.sleep(1)

    print('...checking reservation...')
    if randint(0, 1) == 0:
        result = yield from waitlist_state(name)
    else:
        result = yield from seated_state(name)

    return 'Reserved State calling %s' % result


@asyncio.coroutine
def walkin_state():
    print('No problem, please wait for a moment.')
    time.sleep(1)

    print('...checking availability...')
    if randint(0, 1) == 0:
        result = yield from waitlist_state()
    else:
        result = yield from seated_state()

    return 'Walk-in State calling %s' % result


@asyncio.coroutine
def waitlist_state(name=None):
    if name:
        print('Sorry, we are fully booked for now. We can put %s on the waitlist.' % name)
    else:
        print('Sorry, we are fully booked for now. We can put you on the waitlist.')
    time.sleep(1)

    input_value = yield from get_input('Do you want to be on the waitlist? (y/n) ')
    if input_value.lower() == 'y':
        print('Great, we will let you know when a table becomes available.')
        return 'Waitlist State with name %s' % name if name else 'Waitlist State'
    else:
        print('Okay, have a nice day!')
        return 'End State'


@asyncio.coroutine
def seated_state(name=None):
    print('We have a table available. Please follow me.')
    time.sleep(1)

    if name:
        print('Thank you, %s. Enjoy your meal!' % name)
    else:
        print('Thank you, enjoy your meal!')

    input_value = yield from get_input('Would you like to order now? (y/n) ')
    if input_value.lower() == 'y':
        result = yield from order_state()
    else:
        result = 'End State'

    return 'Seated State with name %s calling %s' % (name, result) if name else 'Seated State calling %s' % result


@asyncio.coroutine
def order_state():
    print('Please tell me what you would like to order.')
    time.sleep(1)

    input_value = yield from get_input('Order: ')
    print('...processing order...')
    time.sleep(1)

    print('Your order of %s has been received. It will be ready soon.' % input_value)
    return 'End State'


@asyncio.coroutine
def get_input(prompt):
    return input(prompt)


if __name__ == '__main__':
    print('Restaurant Simulation with Asyncio Coroutine State Machine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())

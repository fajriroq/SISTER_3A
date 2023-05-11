import asyncio
import time
from random import randint


@asyncio.coroutine
def start_state():
    print('Welcome to our employee management system!')
    input_value = yield from get_input('What would you like to do? (1) Add Employee, (2) Remove Employee: ')

    if input_value == '1':
        result = yield from add_employee_state()
    elif input_value == '2':
        result = yield from remove_employee_state()
    else:
        print('Invalid input.')
        result = yield from start_state()

    print('Resume of the Transition: \nStart State calling ' + result)


@asyncio.coroutine
def add_employee_state():
    print('Please enter the new employee information:')
    name = yield from get_input('Name: ')
    position = yield from get_input('Position: ')
    time.sleep(1)

    print('Adding new employee...')
    if randint(0, 1) == 0:
        print(f'{name} has been added as a {position}.')
        return 'End State'
    else:
        print(f'Sorry, {name} could not be added at this time.')
        return 'Start State'


@asyncio.coroutine
def remove_employee_state():
    print('Please enter the employee information to remove:')
    name = yield from get_input('Name: ')
    position = yield from get_input('Position: ')
    time.sleep(1)

    print('Removing employee...')
    if randint(0, 1) == 0:
        print(f'{name} has been removed from the {position} position.')
        return 'End State'
    else:
        print(f'Sorry, {name} could not be removed at this time.')
        return 'Start State'


@asyncio.coroutine
def get_input(prompt):
    return input(prompt)


if __name__ == '__main__':
    print('Employee Management System Simulation with Asyncio Coroutine State Machine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())

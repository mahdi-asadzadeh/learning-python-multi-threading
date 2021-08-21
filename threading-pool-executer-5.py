from concurrent.futures import ThreadPoolExecutor
from time import sleep, perf_counter
from threading import Thread
from time import sleep


start = perf_counter()


def show(name):
    print(f'Starting - {name}')
    sleep(3)
    print(f'finishing - {name}')


with ThreadPoolExecutor(max_workers=2) as executer:
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
    executer.map(show, names)


end = perf_counter()


print( end - start )

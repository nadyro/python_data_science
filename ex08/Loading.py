from time import sleep
import os

def lst_decorator(lst_elem):
    def wrapper(e, lst):
        txt = str(int(e * 100 / lst.stop)) + '%'
        array = ['' for x in range(int(e * 100 / lst.stop))]
        lst_elem(array, None)

    return wrapper

@lst_decorator
def print_lst_elem(elem, lst):
    print("\r" + str(elem), end = ' ')

def ft_tqdm(lst: range):
    for i in lst:
        print_lst_elem(i, lst)
    print(f'lst.start: {lst.start}')
    print(f'lst.stop: {lst.stop}')
    print(f'lst.step: {lst.step}')
    print(f'\u2588')
    print(os.get_terminal_size())
    return []
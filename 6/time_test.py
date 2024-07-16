from time import time

def exetime(function):
    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        stop = time()

        print(f'{round((stop - start), 2)} s')

    return wrapper
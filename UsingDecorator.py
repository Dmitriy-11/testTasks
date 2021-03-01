def cache(func):
    def inner(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in inner.cache:
            print('calculate value')
            inner.cache[cache_key] = func(*args, **kwargs)
        return inner.cache[cache_key]
    inner.cache = dict()
    return inner


@cache
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


@cache
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


while str != 'n':
    str = input('enter number: (for stop enter "n"): ')
    if str.isdecimal():
        print('result: ', fibonacci(int(str)))

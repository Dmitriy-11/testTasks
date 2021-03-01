def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(23))

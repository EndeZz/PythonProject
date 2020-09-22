# Декоратор с аргументами оборачиваемой функции
def square(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res ** 2
    return wrapper


# Декоратор, который сам может принимать аргументы
def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = 1
            for i in range(power):
                res *= func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@square
def f2(a, b, c):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)) and (c, (float, int)):
        return a + b + c
    return []


@pow(power=3)
def f3(a, b):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        return a - b
    return []

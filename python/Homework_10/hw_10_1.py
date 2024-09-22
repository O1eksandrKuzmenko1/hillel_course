from typing import Generator


def some_gen(begin: int, end: int, func) -> Generator[int, None, float]:

    current = begin
    for _ in range(end):
        yield current
        current = func(current)


def pow(x: int | float) -> int | float:
    return x ** 2


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
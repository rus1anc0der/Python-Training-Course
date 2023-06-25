"""✔Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fibonacci_generator():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fib_iter = iter(fibonacci_generator())
for _ in range(10):
    print(next(fib_iter))

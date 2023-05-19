from numba import jit
from time import time_ns

@jit(nopython=True)
def fibonacci(num):
    if num <= 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

# fibonacci(42)
start = time_ns()
v = fibonacci(42)
end = time_ns()
print(f'{v} time: {(end - start) / 1000000000}s')

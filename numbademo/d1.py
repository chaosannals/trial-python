from numba import jit
from time import time_ns
import numpy as np

x = np.arange(100).reshape(10, 10)

# 只执行一次的话注释 @jit 掉更快。因为第一次要编译。
@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def go_fast(a): # Function is compiled to machine code when called the first time
    trace = 0.0
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i]) # Numba likes NumPy functions
    return a + trace              # Numba likes NumPy broadcasting

start = time_ns()
v = go_fast(x)
end = time_ns()
print(f'{v} time: {(end - start) / 1000000000}s')

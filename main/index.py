import time
import random

def timing(action):
    start = time.time()
    action()
    end = time.time()
    return end - start

def random_set(length, min=1, max=10000000):
    result = set()
    while len(result) < length:
        while True:
            n = random.randint(min, max)
            if n not in result:
                result.add(n)
                break
    return result

a = random_set(1000000)
b = random_set(1000000)

print(timing(lambda : a & b))
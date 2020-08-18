import random

def random_set(length, min=1, max=10000000):
    result = set()
    while len(result) < length:
        while True:
            n = random.randint(min, max)
            if n not in result:
                result.add(n)
                break
    return result
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

def random_list(length, min=1, max=100000000):
    result = []
    while len(result) < length:
        n = random.randint(min, max)
        result.append(n)
    return result
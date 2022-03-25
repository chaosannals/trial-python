def list_chunk(data, length):
    return [data[i: i + length] for i in range(0, len(data), length)]


a = range(123)
b = list_chunk(a, 12)
c = [i for i in range(123)]
d = list_chunk(c, 12)
print(b)
print(d)
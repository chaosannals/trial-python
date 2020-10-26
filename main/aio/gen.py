def gen():
    for i in range(100):
        j = yield i * 2 # 返回 i * 2 出去，接收 send 的值给 j，调用 next 后在调用 next 期间没有 send 则 j 为 None。
        print(f'g: {i} => {j}')

g = gen()
print(f's: {g.send(None)}') # send 之前没有 next 必须传 None。
print(f'n1: {next(g)}')
print(f'n2: {next(g)}')
print(f's: {g.send(10)}') # send 可以给 yield 
print(f'n3: {next(g)}')
print(f's: {g.send(20)}')

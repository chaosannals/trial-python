def gen():
    for i in range(100):
        j = yield i * 2 # 返回 i * 2 出去，接收 send 的值给 j，调用 next 后在调用 next 期间没有 send 则 j 为 None。
        print(f'g: {i} => {j}')

# next 导致生成器从正常流程开始。
# send 会从返回流程开始。 也就是 j 被赋值后开始。

g = gen()
print(f's: {g.send(None)}') # send 之前没有 next 必须传 None。
print(f'n1: {next(g)}')
print(f'n2: {next(g)}')
print(f's: {g.send(10)}') # send 可以给 yield 
print(f'n3: {next(g)}')
print(f's: {g.send(20)}')

def gen_from():
    # from 可以直接转接生成器。
    yield from gen()

gf = gen_from()
print(f'gf s: {gf.send(None)}')
print(f'gf n1: {next(gf)}')
print(f'gf n2: {next(gf)}')
print(f'gf s: {gf.send(10)}')
print(f'gf n3: {next(gf)}')
print(f'gf s: {gf.send(20)}')


import time

try:
    for i in range(10):
        time.sleep(2.0)
        print(f'{i} times sleep 2s')
except KeyboardInterrupt as e:
    print(f'k {e}')
else: # 没有异常则继续的代码
    print('else code')
finally:
    print('finally')
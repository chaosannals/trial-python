from multiprocessing import Process


def work(name):
    print('hello', name)


if __name__ == '__main__':
    process = Process(target=work, args=('test',))
    process.start()
    process.join()

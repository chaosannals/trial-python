from multiprocessing import Pool

def work(x):
    return x * x

if __name__ == '__main__':
    with Pool(5) as pool:
        print(pool.map(work, [1,2,3]))
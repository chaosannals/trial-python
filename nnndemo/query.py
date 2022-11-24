from random import randint
from nnn.base import NumNeuralNetwork
from nnn.mnist import MnistDataSet

def main():
    data_set = MnistDataSet(
        'assets/t10k-labels-idx1-ubyte.gz',
        'assets/t10k-images-idx3-ubyte.gz',
        10
    )
    data_set.ensure_data_set()

    n = NumNeuralNetwork()
    for i in range(10):
        index = randint(0, data_set.count() - 1)
        d = data_set.get_one(index)
        r = n.query(d.image)
        print(f'{index}.jpg {d.label.argmax()} => {r.argmax()}')

if '__main__' == __name__:
    main()
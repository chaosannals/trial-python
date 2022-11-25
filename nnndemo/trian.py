from nnn.base import NumNeuralNetwork
from nnn.mnist import MnistDataSet

def main():
    data_set = MnistDataSet(
        'assets/train-labels-idx1-ubyte.gz',
        'assets/train-images-idx3-ubyte.gz',
        10
    )
    data_set.ensure_data_set()
    data_count = data_set.count()

    n = NumNeuralNetwork(
        input_shape=28 * 28,
        hidden_shape=100,
        output_shape=10,
        learning_rate=0.0014,
    )
    for i in range(10):
        print(f'epoch {i} start')
        for j in range(data_count):
            d = data_set.get_one(j)
            r = n.train(d.image, d.label)
            #print(r)
        print(f'epoch {i} end: {r}')
    n.save()

if '__main__' == __name__:
    main()
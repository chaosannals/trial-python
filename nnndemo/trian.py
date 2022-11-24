from nnn.base import NumNeuralNetwork
from nnn.mnist import MnistDataSet

def main():
    data_set = MnistDataSet(
        'assets/train-labels-idx1-ubyte.gz',
        'assets/train-images-idx3-ubyte.gz',
        10
    )
    data_set.ensure_data_set()

    n = NumNeuralNetwork(
        input_shape=28 * 28,
        hidden_shape=100,
        output_shape=10,
        learning_rate=0.0014,
    )
    for i in range((int)(data_set.count() / 100)):
        print(f'epoch {i} start')
        for j in range(100):
            index = i * 100 + j
            d = data_set.get_one(index)
            r = n.train(d.image, d.label)
            #print(r)
        print(f'epoch {i} end: {r}')
    n.save()

if '__main__' == __name__:
    main()
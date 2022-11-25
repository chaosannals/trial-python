from nnn.base import NumNeuralNetwork
from nnn.selfwrite import load_selfwrite

def main():
    data_set = load_selfwrite('assets/selfwrite/*.png')
    data_count = len(data_set)

    n = NumNeuralNetwork(
        model_path='nnnsw_model.json',
        input_shape=28 * 28,
        hidden_shape=100,
        output_shape=10,
        learning_rate=0.0014,
    )
    for i in range(1000):
        print(f'epoch {i} start')
        for j in range(data_count):
            label, image, _ = data_set[j]
            r = n.train(image, label)
            #print(r)
        print(f'epoch {i} end: {r}')
    n.save()

if '__main__' == __name__:
    main()
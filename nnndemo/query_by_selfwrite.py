from random import randint
from nnn.base import NumNeuralNetwork
from nnn.selfwrite import load_selfwrite

def main():
    data_set = load_selfwrite('assets/selfwrite/*.png')
    data_count = len(data_set)

    n = NumNeuralNetwork()
    for i in range(10):
        index = randint(0, data_count - 1)
        label, image, label_raw = data_set[index]
        r = n.query(image)
        print(f'?-{label_raw}.jpg => {r.argmax()} => {label.argmax()}')

if '__main__' == __name__:
    main()
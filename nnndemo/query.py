from nnn.base import NumNeuralNetwork

def main():
    n = NumNeuralNetwork()
    r = n.query([1.0, 0.5, -1.5])
    print(r)

if '__main__' == __name__:
    main()
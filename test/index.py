from unittest import TestCase, main, skipIf
from trial.index import random_set
from trial.kit import timing

class IndexTest(TestCase):
    '''
    '''

    @skipIf(__name__ != '__main__', 'test')
    def test_random_set(self):
        a = random_set(1000000)
        b = random_set(1000000)
        t = timing(lambda : a & b)
        self.assertGreater(t , 0)


if __name__ == '__main__':
    main()
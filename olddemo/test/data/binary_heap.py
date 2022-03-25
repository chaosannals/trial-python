import random
from unittest import IsolatedAsyncioTestCase, skip
from trial.data import binary_heap
from trial.index import random_list

class MinBinaryHeapTest(IsolatedAsyncioTestCase):
    '''
    '''

    def setUp(self):
        data = [random.randint(1, 100) for _ in range(100)]
        self.bh = binary_heap.MinBinaryHead(data)

    async def test_insert_and_remove(self):
        a = 0
        for _ in range(10):
            v = random.randint(10, 200)
            self.bh.insert(v)
        while self.bh.count() > 0:
            b = self.bh.remove()
            self.assertLessEqual(a, b)
            a = b
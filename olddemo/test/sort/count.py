from unittest import IsolatedAsyncioTestCase, skip
from trial.sort import count
from trial.index import random_list

class CountTest(IsolatedAsyncioTestCase):
    '''
    '''

    @skip('util')
    async def assert_sort(self, r):
        for i in range(len(r) - 1):
            self.assertGreaterEqual(r[i + 1], r[i])

    def setUp(self):
        self.s = random_list(1000, 1, 10000)

    async def test_count_sort(self):
        r = count.count_sort(self.s)
        await self.assert_sort(r)

    async def test_count_sort_1(self):
        r = count.count_sort_1(self.s)
        await self.assert_sort(r)
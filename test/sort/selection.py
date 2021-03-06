from unittest import IsolatedAsyncioTestCase, skip
from trial.sort import selection
from trial.index import random_list

class SelectionTest(IsolatedAsyncioTestCase):
    '''
    '''

    @skip('util')
    async def assert_sort(self, r):
        for i in range(len(r) - 1):
            self.assertGreaterEqual(r[i + 1], r[i])

    def setUp(self):
        self.s = random_list(1000)

    async def test_selection_sort(self):
        r = selection.selection_sort(self.s)
        await self.assert_sort(r)
from unittest import IsolatedAsyncioTestCase, skip
from trial.sort import insert
from trial.index import random_list

class InsertTest(IsolatedAsyncioTestCase):
    '''
    '''

    @skip('util')
    async def assert_sort(self, r):
        for i in range(len(r) - 1):
            self.assertGreaterEqual(r[i + 1], r[i])

    def setUp(self):
        self.s = random_list(1000)

    async def test_insert_sort(self):
        r = insert.insert_sort(self.s)
        await self.assert_sort(r)

    async def test_shell_sort(self):
        r = insert.shell_sort(self.s)
        await self.assert_sort(r)
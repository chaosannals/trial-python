from unittest import IsolatedAsyncioTestCase, skip
from trial.sort import bubble
from trial.index import random_list


class BubbleTest(IsolatedAsyncioTestCase):
    '''
    '''

    @skip('util')
    async def assert_sort(self, r):
        for i in range(len(r) - 1):
            self.assertGreaterEqual(r[i + 1], r[i])

    def setUp(self):
        self.s = random_list(1000)

    async def test_bubble_sort(self):
        r = bubble.bubble_sort(self.s)
        await self.assert_sort(r)

    async def test_bubble_sort_1(self):
        r = bubble.bubble_sort_1(self.s)
        await self.assert_sort(r)

    async def test_bubble_sort_2(self):
        r = bubble.bubble_sort_2(self.s)
        await self.assert_sort(r)

    async def test_cocktail_sort(self):
        r = bubble.cocktail_sort(self.s)
        await self.assert_sort(r)

    async def test_cocktail_sort_1(self):
        r = bubble.cocktail_sort_1(self.s)
        await self.assert_sort(r)

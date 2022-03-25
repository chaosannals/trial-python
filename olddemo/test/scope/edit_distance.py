from unittest import IsolatedAsyncioTestCase, skip
from trial.score import edit_distance
from trial.index import random_list


class HashMapTest(IsolatedAsyncioTestCase):
    '''
    '''

    async def test_recursion(self):
        r = edit_distance.edit_distance_r('hello', 'helio-world')
        self.assertEqual(r, 7)

    async def test_loop(self):
        r = edit_distance.edit_distance('hello', 'helio-world')
        self.assertEqual(r, 7)

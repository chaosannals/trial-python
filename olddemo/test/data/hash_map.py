from unittest import IsolatedAsyncioTestCase, skip
from trial.data import hash_map
from trial.index import random_list

class HashMapTest(IsolatedAsyncioTestCase):
    '''
    '''

    def setUp(self):
        self.hm = hash_map.IntHashMap()
        self.hm.put(3, 'aaaa')
        self.hm.put(12, 'bbbb')
        self.hm.put(35, 'cccc')

    async def test_get(self):
        self.assertEqual(self.hm.get(3), 'aaaa')
        self.assertEqual(self.hm.get(12), 'bbbb')
        self.assertEqual(self.hm.get(35), 'cccc')

    async def test_reset(self):
        self.hm.resize(6)
        self.assertEqual(self.hm.get(3), 'aaaa')
        self.assertEqual(self.hm.get(12), 'bbbb')
        self.assertEqual(self.hm.get(35), 'cccc')
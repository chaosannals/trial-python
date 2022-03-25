import math


class MinBinaryHead:
    '''
    最小二叉堆。
    '''

    def __init__(self, data=None):
        '''
        初始化，对堆做排序。
        '''

        self.data = data if None != data else []
        count = len(self.data)
        if count > 1:
            for i in range(math.ceil(count / 2), -1, -1):
                self.adjust_down(i, count)

    def insert(self, item):
        '''
        插入。
        '''

        self.data.append(item)
        self.adjust_up()

    def remove(self):
        '''
        删除。
        '''

        head = self.data[0]
        tail = self.data.pop()
        count = len(self.data)
        if count > 1:
            self.data[0] = tail
            for i in range(math.ceil(count / 2), -1, -1):
                self.adjust_down(i, count)
        return head

    def count(self):
        '''
        堆数据总数。
        '''

        return len(self.data)

    def adjust_up(self):
        '''
        从末端向上，把最小元素弄到顶部。
        '''

        target = len(self.data) - 1
        parent = math.floor((target - 1) / 2)
        tmp = self.data[target]
        while target > 0 and tmp < self.data[parent]:
            self.data[target] = self.data[parent]
            target = parent
            parent = math.floor((target - 1) / 2)
        self.data[target] = tmp

    def adjust_down(self, parent, length):
        '''
        指定开始点，把比他小的元素顶上来。
        '''

        tmp = self.data[parent]
        target = 2 * parent + 1
        while target < length:
            n = target + 1
            if n < length and self.data[n] < self.data[target]:
                target += 1
            if tmp < self.data[target]:
                break
            self.data[parent] = self.data[target]
            parent = target
            target = 2 * parent + 1
        self.data[parent] = tmp

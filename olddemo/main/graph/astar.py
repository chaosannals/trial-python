import sys
import random


class Graph2D:
    '''
    平面二维图。
    '''

    def __init__(self, width, height):
        '''
        初始化一张 width * height 的全 0 图。
        再随机插入 8 代表终点，9 代表起点。
        '''

        self.width = width
        self.height = height
        self.data = [[0 for _ in range(0, width)] for _ in range(0, height)]
        self.start = self.insert(9)
        self.end = self.insert(8)

    def find(self, position):
        '''
        查找点数据。
        '''

        x = position[0]
        y = position[1]
        if x < 0 or x >= self.width:
            return None
        if y < 0 or y >= self.height:
            return None
        return self.data[y][x]

    def reset(self, position, v):
        '''
        重置点数据。
        '''

        x = position[0]
        y = position[1]
        if x < 0 or x >= self.width:
            return None
        if y < 0 or y >= self.height:
            return None
        self.data[y][x] = v

    def show(self):
        '''
        打印图
        '''

        for i in range(0, self.height):
            for j in range(0, self.width):
                c = str(self.data[i][j])
                sys.stdout.write(c)
            sys.stdout.write('\n')

    def insert(self, v):
        '''
        随机插入到 0 的点。
        '''

        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            c = self.data[y][x]
            if c == 0:
                self.data[y][x] = v
                return (x, y)

    def hinder(self, n):
        '''
        随机插入指定个数的 1 点。
        '''

        for _ in range(0, n):
            self.insert(1)


class AStarNode:
    '''
    节点
    position 坐标
    last 下一个节点

    '''

    def __init__(self, position, g=0, h=0):
        self.position = position
        self.last = None
        self.g = g # 实走距离
        self.h = h # 预估距离
        self.f = g + h # 估计值汇总

    def measure(self, target, last=None):
        '''
        只知道起始两点的情况下做粗略地估算。
        有上一个点时在上个点的基础上加1。
        '''

        xh = abs(target[0] - self.position[0])
        yh = abs(target[1] - self.position[1])
        self.last = last
        self.h = xh + yh
        self.g = last.g + 1 if last != None else 0
        self.f = self.g + self.h

    def at(self, position):
        '''
        判断是否在该位置。
        '''

        return self.position[0] == position[0] and self.position[1] == position[1]

    def get_around(self):
        '''
        给出周围邻接四方的四个点坐标。
        '''

        return [
            self.get_top(),
            self.get_left(),
            self.get_right(),
            self.get_bottom()
        ]

    def get_top(self):
        x = self.position[0]
        y = self.position[1] - 1
        return (x, y)

    def get_left(self):
        x = self.position[0] - 1
        y = self.position[1]
        return (x, y)

    def get_right(self):
        x = self.position[0] + 1
        y = self.position[1]
        return (x, y)

    def get_bottom(self):
        x = self.position[0]
        y = self.position[1] + 1
        return (x, y)


class AStar:
    '''

    '''

    def __init__(self, graph):
        '''
        初始化。
        '''

        start = AStarNode(graph.start)
        start.measure(graph.end)
        self.opens = [start]
        self.closes = []
        self.graph = graph

    def find(self):
        '''
        查找路径。
        '''

        while len(self.opens) > 0:
            m = self.pop_open()
            for i in m.get_around():
                if self.is_close(i) or self.is_open(i):
                    continue
                v = self.graph.find(i)
                if v == 0:
                    n = AStarNode(i)
                    n.measure(self.graph.end, m)
                    self.opens.append(n)
                elif v == 8:
                    return m

    def show(self):
        '''
        把路径在图上绘制出来。
        '''

        m = self.find()
        while m != None:
            v = self.graph.find(m.position)
            if v == 0:
                self.graph.reset(m.position, 7)
            m = m.last

    def pop_open(self):
        '''
        开集拿出处理点，并加入闭集。
        '''

        m = None
        index = 0
        length = len(self.opens)
        if length == 0:
            return None
        for i in range(0, length):
            item = self.opens[i]
            if m == None or m.f > item.f:
                m = item
                index = i
        r = self.opens.pop(index)
        self.closes.append(r)
        return r

    def is_open(self, position):
        '''
        是否在开集里。
        '''

        for i in self.opens:
            p = i.position
            if p[0] == position[0] and p[1] == position[1]:
                return True
        return False

    def is_close(self, position):
        '''
        是否在闭集里。
        '''

        for i in self.closes:
            p = i.position
            if p[0] == position[0] and p[1] == position[1]:
                return True
        return False


graph = Graph2D(80, 80)
graph.hinder(500)
astar = AStar(graph)
astar.show()
graph.show()

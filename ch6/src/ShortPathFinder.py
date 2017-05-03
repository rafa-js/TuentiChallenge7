from heapdict import heapdict

from ch6.src import Tower


class ShortPathFinder:
    def __init__(self):
        self.floors = 0
        self.edges = {}
        self.ShortNodes = []


    def find_shortest_path(self, tower: Tower) -> int:
        self.floors = tower.Floors
        self.floors = tower.Floors
        self.edges = {}
        for s in tower.Shortcuts:
            a, b, y = s
            if self.get_movement_cost(a, b) >= y:
                if a not in self.edges:
                    self.edges[a] = []
                self.edges[a].append((b, y))
        self.ShortNodes = sorted(self.edges.keys())
        return self.dijkstra(1, tower.Floors)


    def dijkstra(self, start: int, end: int):
        v = start
        Distances = {start: 0}
        Open = heapdict()
        Open.keys()
        Open[start] = 0
        Closed = set()
        while len(Open) > 0 and v != end:
            v = Open.popitem()[0]
            if v not in Closed:
                Closed.add(v)
                for s in self.get_movements(v):
                    f, y = s
                    if f not in Closed:
                        Y = Distances[v] + y
                        if f not in Distances or Distances[f] >= Y:
                            Distances[f] = Y
                            if f not in Open or Y < Open[f]:
                                Open[f] = Y
        return Distances[v]


    def get_movements(self, f):
        movs = self.binary_search(self.ShortNodes, f)
        if f in self.edges:
            for e in self.edges[f]: movs.append(e)
        return movs


    def binary_search(self, values, key):
        if len(values) == 0:
            return [(self.floors, self.get_movement_cost(key, self.floors))]
        if len(values) == 1:
            movs = []
            if key > values[0]:
                movs.append((values[0], 0))
                movs.append((self.floors, self.get_movement_cost(key, self.floors)))
            if key < values[0]:
                if key > 1:
                    movs.append((1, 0))
                movs.append((values[0], self.get_movement_cost(key, values[0])))
            else:
                movs.append((1, 0))
                movs.append((self.floors, self.get_movement_cost(key, self.floors)))
            return movs
        lo = 0
        hi = len(values) - 1
        movs = []
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if values[mid] == key:
                if mid > 0:
                    movs.append((values[mid - 1], 0))
                elif key > 1:
                    movs.append((1, 0))
                if mid < len(values) - 1:
                    movs.append((values[mid + 1], self.get_movement_cost(key, values[mid + 1])))
                else:
                    movs.append((self.floors, self.get_movement_cost(key, self.floors)))
                return movs
            if values[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1
        if hi < 0:
            if key > 1:
                movs.append((1, 0))
            movs.append((values[0], self.get_movement_cost(key, values[0])))
        elif lo >= len(values):
            movs.append((values[-1], 0))
            movs.append((self.floors, self.get_movement_cost(key, self.floors)))
        else:
            movs.append((values[hi], 0))
            movs.append((values[lo], self.get_movement_cost(key, values[lo])))
        return movs
        raise Exception('What the hell?!')


    def get_movement_cost(self, a, b):
        return b * (b - 1) // 2 - a * (a - 1) // 2

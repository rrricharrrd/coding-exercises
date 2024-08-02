from ._exception import DataStructureException


class HeapError(DataStructureException):
    pass


class Heap:
    def __init__(self):
        self.nodes = []

    def __str__(self):
        return f"Heap<{self.nodes}>"

    def is_empty(self):
        return not bool(self.nodes)

    def peek(self):
        if self.is_empty():
            raise HeapError("Empty heap")

        return self.nodes[0]

    def extract_min(self):
        pass
        # result = self.nodes[0]
        # self.nodes[0] = self.nodes[-1]

    def insert(self, data):
        self.nodes.append(data)
        current = len(self.nodes) - 1
        parent = current // 2
        done = False
        while current != 0 and not done:
            if self.nodes[parent] > self.nodes[current]:
                self.nodes[parent], self.nodes[current] = self.nodes[current], self.nodes[parent]
            else:
                done = True
            current = parent
            parent = parent // 2

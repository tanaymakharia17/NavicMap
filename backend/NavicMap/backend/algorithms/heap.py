class Heap:

    def __init__(self, type):
        self.minHeap = []
        self.type = False if type == "min" else True

    def size(self):
        return len(self.minHeap)

    def clear(self):
        self.minHeap.clear()

    def cnd(self, x, y):
        if self.type:
            return x < y
        return x > y

    def heapify(self, idx):
        n = self.size()
        array = self.minHeap
        largest = idx
        l = (2 * idx + 1 if 2 * idx + 1 < n else idx)
        r = (2 * idx + 2 if 2 * idx + 2 < n else idx)
        if self.cnd(array[largest], array[l]):
            largest = l
        if self.cnd(array[largest], array[r]):
            largest = r
        if largest != idx:
            array[idx], array[largest] = array[largest], array[idx]
            self.heapify(largest)

    def push(self, x):
        self.minHeap.append(x)
        n = n = self.size()
        ptr = n-1
        while ptr > 0:
            tmp = ptr//2
            if self.cnd(self.minHeap[tmp], self.minHeap[ptr]):
                self.minHeap[tmp], self.minHeap[ptr] = self.minHeap[ptr], self.minHeap[tmp]
            ptr = tmp

    def isEmpty(self):
        return False if self.size() != 0 else True

    def top(self):
        return self.minHeap[0]

    def pop(self):
        tmpValue = self.minHeap[0]
        back = self.minHeap.pop()
        n = self.size()
        if n > 0:
            self.minHeap[0] = back
            self.heapify(0)
        return tmpValue
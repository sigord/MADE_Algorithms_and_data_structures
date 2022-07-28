import sys


class MinHeap(object):
    """
    Heap with min on top
    Data shape (n, 1): [[item1, ...], [item2, ...], ...]
    """

    def __init__(self):
        self.array = []
        self.size = 0

    def siftUp(self, i):
        while i > 0 and self.array[i][0] < self.array[int((i - 1) / 2)][0]:
            self.array[i], self.array[int((i - 1) / 2)] = self.array[int((i - 1) / 2)], self.array[i]
            i = int((i - 1) / 2)
    
    def siftDown(self, i):
        while 2 * i + 1 < self.size:
            cur = self.array[i][0]
            left = self.array[2 * i + 1][0]
            if 2 * i + 2 == self.size:
                right = sys.maxsize
            else:
                right = self.array[2 * i + 2][0]
            if left <= right and left < cur:
                self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
                i = 2 * i + 1
            elif right < left and right < cur:
                self.array[i], self.array[2 * i + 2] = self.array[2 * i + 2], self.array[i]
                i = 2 * i + 2
            else:
                break


    def insert(self, item):
        """Add item to end of heap"""

        i = self.size
        self.array.append(item)
        self.size += 1

        self.siftUp(i)

    def removeMin(self):
        """Remove min item"""

        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        del self.array[self.size - 1]
        self.size -= 1
        i = 0
        self.siftDown(i)

  
############ ---- Main Block ---- ############

heap = MinHeap()
command_index = 0
result = list()
for line in sys.stdin:
    if '\n' == line.rstrip():
        break
    
    command_index += 1
    command = str(line)[:-1].split()

    if command[0] == "push":
        heap.insert(item = [int(command[1]), command_index])
    elif command[0] == "extract-min":
        if heap.size == 0:
            result.append("*")
        else:
            out = list(map(str, heap.array[0]))
            result.append(out[0] + ' ' + out[1])
            heap.removeMin()
    elif command[0] == "decrease-key":
        for i in range(heap.size):
            if heap.array[i][1] == int(command[1]):
                heap.array[i][0] = int(command[2])
                heap.siftUp(i)
                break

print(*result, sep='\n')
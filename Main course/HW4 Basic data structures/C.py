import sys


class DinamicCyclicArray(object):

    def __init__(self):
        self.begin = 0
        self.end = 0
        self.size = 0
        self.capacity = 1  # Avaible space
        self.array = self.make_array(self.capacity)  # [begin, end)

    def next(self, i):
        return (i + 1) % self.capacity

    def make_array(self, new_capacity):
        """Return array"""
        return [None] * new_capacity

    def __len__(self):
        """Return length of array"""
        return self.size
        # не разобрался как писать условия для случая,
        # когда size == capacity поэтому решил хранить size
        # return (self.end + self.capacity - self.begin) % self.capacity

    def __getitem__(self, index):
        """Return the elemen at given index"""

        if not 0 <= index < self.size:
            raise IndexError(
                'Given index = {0} is larger than array size = {1}'.format(
                    index, self.size))

        if self.begin == 0:
            return self.array[index]
        elif self.begin < self.end:
            return self.array[index + self.begin]
        elif self.begin > self.end:
            if self.begin + index < self.capacity:
                return self.array[index + self.begin]
            else:
                return self.array[index + self.begin - self.capacity]

    def _resize(self, new_capacity):
        """Resize the array with new capacity"""
        new_array = self.make_array(new_capacity)

        index = 0
        old_index = self.begin
        while index < self.size:
            new_array[index] = self.array[old_index]
            old_index = self.next(old_index)
            index += 1

        self.array = new_array
        self.capacity = new_capacity
        self.begin = 0
        self.end = self.size % self.capacity

    def append(self, item):
        """Add item to end of array"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.end] = item
        self.size += 1
        self.end = self.next(self.end)

    def erase(self):
        """Delete item from the beginning of array"""

        if self.size == 0:
            print("Array is empty deletion not possible")
            return

        self.array[self.begin] = None
        self.begin = self.next(self.begin)
        self.size -= 1

        if self.size <= self.capacity // 4 and self.capacity > 1:
            self._resize(self.capacity // 2)

    def __str__(self):
        out = '['
        if self.size == 0:
            out = out + ']'
            return out
        else:
            i = 0
            index = self.begin
            while i < self.size - 1:
                out = out + str(self.array[index]) + ', '
                index = self.next(index)
                i += 1
            out = out + str(self.array[index]) + ']'
            return str(out)


class DinamicArrayQueue:
    def __init__(self, iterable=None):
        self.array = DinamicCyclicArray()

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        """Insert item to end of queue"""

        self.array.append(item)

    def pop(self):
        """Remove first item in queue"""

        self.array.erase()

    def __len__(self):
        """Return size of stack"""
        return self.array.size

    def head(self):
        """Return the first item in queue"""

        return self.array.array[self.array.begin]

    def __str__(self):
        return str(self.array.__str__())


############ ---- Input Optimizations ---- ############


input = sys.stdin.readline


def inp():
    return(int(input()))


def str_inp():
    return(str(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


############ ---- Main Block ---- ############

operations = inp()
aq = DinamicArrayQueue()


for i in range(operations):

    str_ = str_inp()
    if str_[0] == "+":
        tag, elem = map(str, str_.split(sep=' '))
        elem = int(elem)
    elif str_[0] == "-":
        tag = str_[0]

    if tag == "+":
        aq.push(item=elem)
    elif tag == "-":
        sys.stdout.write(str(aq.head()) + "\n")
        aq.pop()
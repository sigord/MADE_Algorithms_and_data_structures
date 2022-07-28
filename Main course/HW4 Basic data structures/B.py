import sys


class DinamicArray(object):

    def __init__(self):
        self.size = 0  # Actual number of elements
        self.capacity = 1  # Avaible space
        self.array = self.make_array(self.capacity)

    def make_array(self, new_capacity):
        """Return array"""
        return [None] * new_capacity

    def __len__(self):
        """Return length of array"""
        return self.size

    def __getitem__(self, index):
        """Return the elemen at given index"""
        if not 0 <= index < self.size:
            raise IndexError(
                'Given index = {0} is larger than array size = {1}'.format(
                    index, self.size))

        return self.array[index]

    def _resize(self, new_capacity):
        """Resize the array with new capacity"""
        new_array = self.make_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        """Add item to end of array"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = item
        self.size += 1

    def erase(self):
        """Delete item from the end of array"""

        if self.size == 0:
            print("Array is empty deletion not possible")
            return

        self.array[self.size - 1] = None
        self.size -= 1

        if self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)

    def __str__(self):
        return str(self.array[:self.size])


class DinamicArrayStack:
    def __init__(self, iterable=None):
        self.array = DinamicArray()

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        """Insert item on top of stack"""

        self.array.append(item)

    def pop(self):
        """Remove top item"""

        self.array.erase()

    def __len__(self):
        """Return size of stack"""
        return self.array.size

    def back(self):
        """Return the item on the top"""

        return self.array.array[self.array.size - 1]

    def __str__(self):
        return str(self.array.array[:self.array.size])


############ ---- Input Optimizations ---- ############


input = sys.stdin.readline


def inp():
    return(int(input()))


def str_inp():
    return(str(input()))


def inlt():
    return(list(map(str, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


############ ---- Main Block ---- ############

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


postfix_list = inlt()

ArrS = DinamicArrayStack()

for i in range(len(postfix_list)):
    if is_int(postfix_list[i]):
        ArrS.push(int(postfix_list[i]))
    elif postfix_list[i] == "+":
        second = ArrS.back()
        ArrS.pop()
        first = ArrS.back()
        ArrS.pop()
        ArrS.push(item=(first + second))
    elif postfix_list[i] == "-":
        second = ArrS.back()
        ArrS.pop()
        first = ArrS.back()
        ArrS.pop()
        ArrS.push(item=(first - second))
    elif postfix_list[i] == "*":
        second = ArrS.back()
        ArrS.pop()
        first = ArrS.back()
        ArrS.pop()
        ArrS.push(item=(first * second))

print(ArrS.back())
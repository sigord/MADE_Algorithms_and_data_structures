import sys


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, item):
        """Insert item into tail"""

        new_node = Node(item, None)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def erase(self, index):
        """Delete elem by index"""

        if index + 1 > self.size or index < 0:
            raise IndexError('Index is out of bounds: {}'.format(index))

        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            prev = self.head
            cur = prev.next
            j = 1
            while j < index:
                prev = cur
                cur = prev.next
                j += 1
            prev.next = cur.next
            if cur == self.tail:
                self.tail = prev

        self.size -= 1

    def get_size(self):
        return self.size

    def __str__(self):
        if self.head is not None:
            cur = self.head
            next_ = cur.next
            out = str(cur.data) + '\n'
            while next_.next is not None:
                cur = cur.next
                next_ = next_.next
                out += str(cur.data) + '\n'
            out += str(next_.data)
            return out
        return 'List is empty'


class LinkedStack:
    def __init__(self, iterable=None):
        self.list = LinkedList()

        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        """Insert item on top of stack"""

        new_node = Node(item, self.list.head)
        self.list.head = new_node
        self.list.size += 1

    def pop(self):
        """Remove top item"""

        if self.list.head is None or self.list.head is None:
            self.list.head = None
            self.list.tail = None
            self.list.size = 0
        else:
            self.list.head = self.list.head.next
            self.list.size -= 1

    def get_size(self):
        """Return size of stack"""

        return self.list.get_size()

    def back(self):
        """Return the item on the top"""

        return self.list.head.data

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
ls = LinkedStack()
result = list()

for i in range(operations):

    str_ = str_inp()
    if int(str_[0]) == 1:
        tag, elem = map(int, str_.split(sep=' '))
    else:
        tag = int(str_)

    if tag == 1:
        if ls.get_size() == 0:
            ls.push(item=elem)
        else:
            ls.push(item=min(ls.back(), elem))
    elif tag == 2:
        ls.pop()
    elif tag == 3:
        sys.stdout.write(str(ls.back()) + "\n")
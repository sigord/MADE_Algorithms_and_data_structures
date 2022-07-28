import sys
INITIAL_CAPACITY = 10**6 * 2
SEPARATOR = "\n"
UNICODE = "utf-8"


class Node():
    """Node with global double links"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.global_next = None
        self.global_prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class HashTable():
    """
    Hash table
    Resolving collisions by separate chaining
    """

    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """
        Generate a hash for a given key
        Input:  key - string
        Output: Index from 0 to self.capacity
        """
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value, g_prev):
        """
        Insert a key,value pair to the hashtable
        Input:  key - string, value - anything, global last node
        Output: Return the node
        """

        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            if g_prev is None:

                self.buckets[index] = Node(key, value)
                return self.buckets[index]
            else:

                self.buckets[index] = Node(key, value)

                curr = self.buckets[index]
                curr.global_prev = g_prev
                g_prev.global_next = curr

                return curr

        local_prev = node
        while node is not None:
            if node.key == key:

                node.value = value

                return g_prev
            local_prev = node
            node = node.next

        local_prev.next = Node(key, value)

        curr = local_prev.next
        curr.global_prev = g_prev
        g_prev.global_next = curr

        return curr

    def remove(self, key, g_last):
        """
        Remove node stored at key
        Input:  key - string, global last node
        Output: global last node
        """

        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:

            return g_last

        else:

            self.size -= 1

            if prev is None:

                curr = node
                if g_last.key == curr.key:

                    if g_last.global_prev is None:

                        g_last = None
                    else:
                        g_last = g_last.global_prev
                        g_last.global_next = None

                else:

                    if curr.global_prev is None:

                        g_next = curr.global_next
                        g_next.global_prev = None

                    else:

                        g_prev = curr.global_prev
                        g_next = curr.global_next

                        g_prev.global_next = g_prev.global_next.global_next
                        g_next.global_prev = g_next.global_prev.global_prev

                self.buckets[index] = node.next

            else:

                curr = node
                if g_last.key == curr.key:

                    if g_last.global_prev is None:

                        g_last = None
                    else:
                        g_last = g_last.global_prev
                        g_last.global_next = None

                else:

                    if curr.global_prev is None:

                        g_next = curr.global_next
                        g_next.global_prev = None

                    else:

                        g_prev = curr.global_prev
                        g_next = curr.global_next

                        g_prev.global_next = g_prev.global_next.global_next
                        g_next.global_prev = g_next.global_prev.global_prev

                prev.next = prev.next.next

            return g_last

    def find_node(self, key):
        """
        Find a node by the key
        Input:  key - string
        Output: node
        """

        index = self.hash(key)

        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        return node

    def find(self, key):
        """
        Find a data value based on key
        Input:  key - string
        Output: value stored under "key" or nothing if not found
        """
        node = self.find_node(key)

        if node is None:
            # Not found
            return "none"
        else:
            # Found - return the data value
            return node.value

    def get_next(self, key):

        node = self.find_node(key)
        if node is None:
            return "none"

        next_node = node.global_next
        if next_node is None:
            return "none"
        else:
            return next_node.value

    def get_prev(self, key):

        node = self.find_node(key)
        if node is None:
            return "none"

        prev = node.global_prev

        if prev is None:
            return "none"
        else:
            return prev.value


############ ---- Main Block ---- ############

def solve():
    map_object = HashTable()
    data = sys.stdin.buffer.readlines()
    result_exists = []
    n_operations = len(data)
    g_prev = None
    for i in range(n_operations):
        command = str(data[i].decode(UNICODE))[:-1].split()

        if command[0] == "put":
            g_prev = map_object.insert(
                str(command[1]), str(command[2]), g_prev)
        elif command[0] == "get":
            result_exists.append(map_object.find(str(command[1])))
        elif command[0] == "delete":
            g_prev = map_object.remove(str(command[1]), g_prev)
        elif command[0] == "prev":
            result_exists.append(map_object.get_prev(str(command[1])))
        elif command[0] == "next":
            result_exists.append(map_object.get_next(str(command[1])))

    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)


if __name__ == "__main__":
    solve()
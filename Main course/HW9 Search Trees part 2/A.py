import sys
from random import Random
SEPARATOR = "\n"
UNICODE = "utf-8"
SEED = 43
random = Random(SEED)
MAX = sys.maxsize
MIN = 0

class TreapNode():
    """Node for tree"""

    def __init__(self, key):
        self.key = key
        self.y = random.randint(MIN, MAX)
        self.left = None
        self.right = None

def split(tree: TreapNode, key):
    if tree is None:
        l_node = None
        r_node = None
        return l_node, r_node
    if tree.key > key:
        l_node, r_node = split(tree.left, key)
        tree.left = r_node
        return l_node, tree
    else:
        l_node, r_node = split(tree.right, key)
        tree.right = l_node
        return tree, r_node
        

def merge(node1: TreapNode, node2: TreapNode):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    if node1.y > node2.y:
        node1.right = merge(node1.right, node2)
        return node1
    else:
        node2.left = merge(node1, node2.left)
        return node2

def insert(tree: TreapNode, node: TreapNode):
    if tree is None:
        return node
    if tree.y > node.y:
        if node.key < tree.key:
            tree.left = insert(tree.left, node)
        elif node.key > tree.key:
            tree.right = insert(tree.right, node)
        return tree
    l_node, r_node = split(tree, node.key)
    node.left = l_node
    node.right = r_node
    return node
    

def search(node: TreapNode, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


def delete(node: TreapNode, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
        return node
    elif key > node.key:
        node.right = delete(node.right, key)
        return node
    else:
        return merge(node.left, node.right)


def findMax(node: TreapNode):
    cur = node
    while cur.right is not None:
        cur = cur.right
    return cur


def findMin(node: TreapNode):
    cur = node
    while cur.left is not None:
        cur = cur.left
    return cur


def printTree(node: TreapNode):
    if node is not None:
        printTree(node.left)
        print(node.key)
        printTree(node.right)


def next(root, key):
    node = root
    res = None
    while node is not None:
        if node.key > key:
            res = node
            node = node.left
        else:
            node = node.right
    return res


def prev(root, key):
    node = root
    res = None
    while node is not None:
        if node.key < key:
            res = node
            node = node.right
        else:
            node = node.left
    return res

############ ---- Main Block ---- ############


def solve():

    data = sys.stdin.buffer.readlines()
    result_list = []
    n_operations = len(data)
    root = None
    for i in range(n_operations):
        command = str(data[i].decode(UNICODE))[:-1].split()
        
        if command[0] == "insert":
            node = TreapNode(int(command[1]))
            if search(root, int(command[1])) is None:
                root = insert(root, node)
        elif command[0] == "delete":
            if search(root, int(command[1])) is not None:
                root = delete(root, int(command[1]))
        elif command[0] == "exists":
            if search(root, int(command[1])) is None:
                result_list.append("false")
            else:
                result_list.append("true")
        elif command[0] == "next":
            next_elem = next(root, int(command[1]))
            if next_elem is None:
                result_list.append("none")
            else:
                result_list.append(str(next_elem.key))
        elif command[0] == "prev":
            prev_elem = prev(root, int(command[1]))
            if prev_elem is None:
                result_list.append("none")
            else:
                result_list.append(str(prev_elem.key))

    encoded_array = (SEPARATOR.join(result_list)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)


if __name__ == "__main__":
    solve()
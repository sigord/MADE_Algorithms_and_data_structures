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

    def __init__(self, val):
        self.size = 1
        self.y = random.randint(MIN, MAX)
        self.left = None
        self.right = None
        self.val = val
        
def size(tree: TreapNode):
    if tree is None:
        return 0
    return tree.size

def update_size(node: TreapNode):
    if node is not None:
        node.size = 1 + size(node.left) + size(node.right)

def split(tree: TreapNode, key):
    if tree is None:
        l_node = None
        r_node = None
        return l_node, r_node
    if size(tree.left) > key:
        l_node, r_node = split(tree.left, key)
        tree.left = r_node
        update_size(tree)
        return l_node, tree
    else:
        l_node, r_node = split(tree.right, key - size(tree.left) - 1)
        tree.right = l_node
        update_size(tree)
        return tree, r_node
        

def merge(node1: TreapNode, node2: TreapNode):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    if node1.y > node2.y:
        node1.right = merge(node1.right, node2)
        update_size(node1)
        return node1
    else:
        node2.left = merge(node1, node2.left)
        update_size(node2)
        return node2

def insert(tree: TreapNode, position, value):
    l, r = split(tree, position)
    node = TreapNode(value)
    return merge(merge(l, node), r)
    

def search(node: TreapNode, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


def delete(node: TreapNode, position):
    l1, r1 = split(node, position)
    l2, r2 = split(l1, position - 1)
    tree = merge(l2, r1)
    return tree


def list2treap(arr):
    node = None
    for i in arr:
        node = merge(node, TreapNode(i))
    return node

def get_value(tree: TreapNode, position):
    index = size(tree.left)
    if position < index:
        return get_value(tree.left, position)
    elif position == index:
        return tree.val
    else:
        return get_value(tree.right, position - index - 1)
    
def to_front(tree, l, r):
    l1, r1 = split(tree, r + 1)
    l2, r2 = split(tree, l)
    return merge(merge(r2, l2), r1)

def print_treap(tree: TreapNode):
    if tree is not None:
        print_treap(tree.left)
        sys.stdout.write(str(tree.val) + " ")
        print_treap(tree.right)
    
    
############ ---- Main Block ---- ############


def solve():

    data = sys.stdin.buffer.readlines()
    result_list = []
    n_operations = len(data)
    root = None
    for i in range(n_operations):
        command = str(data[i].decode(UNICODE))[:-1].split()
        if i == 0:
            initial_len = int(command[0])
            queries = int(command[1])
            continue
        if i == 1:
            arr = list(map(int, command))
            root = list2treap(arr)
            continue
        
        if command[0] == "add":
            position = int(command[1]) - 1
            value = int(command[2])
            root = insert(root, position, value)
        elif command[0] == "del":
            root = delete(root, int(command[1]) - 1)
            
    print(size(root))
    print_treap(root)


if __name__ == "__main__":
    solve()
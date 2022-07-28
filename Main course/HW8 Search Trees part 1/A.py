import sys
SEPARATOR = "\n"
UNICODE = "utf-8"


class TreeNode():
    """Node for tree"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node: TreeNode, key):
    if node is None:
        return TreeNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node


def search(node: TreeNode, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


def delete(node: TreeNode, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    elif node.left is not None and node.right is not None:
        node.key = findMin(node.right).key
        node.right = delete(node.right, node.key)
    elif node.left is not None:
        node = node.left
    elif node.right is not None:
        node = node.right
    else:
        node = None
    return node


def findMax(node: TreeNode):
    cur = node
    while cur.right is not None:
        cur = cur.right
    return cur


def findMin(node: TreeNode):
    cur = node
    while cur.left is not None:
        cur = cur.left
    return cur


def printTree(node: TreeNode):
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
            root = insert(root, int(command[1]))
        elif command[0] == "delete":
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
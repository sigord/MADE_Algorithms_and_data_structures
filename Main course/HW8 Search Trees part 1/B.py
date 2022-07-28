import sys
SEPARATOR = "\n"
UNICODE = "utf-8"

class TreeNode():
    """Node for avl tree"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node: TreeNode):
    if node is not None:
        return node.height
    else:
        return 0

def get_balance_f(node: TreeNode):
    return height(node.right) - height(node.left)

def fixheight(node: TreeNode):
    left_h = height(node.left)
    right_h = height(node.right)
    if left_h > right_h:
        node.height = left_h + 1
    else:
        node.height = right_h + 1

def rotate_right(node: TreeNode):
    q = node.left
    node.left = q.right
    q.right = node
    fixheight(node)
    fixheight(q)
    return q

def rotate_left(node: TreeNode):
    p = node.right
    node.right = p.left
    p.left = node
    fixheight(node)
    fixheight(p)
    return p

def balance(node: TreeNode):
    fixheight(node)
    if get_balance_f(node) == 2:
        if get_balance_f(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    if get_balance_f(node) == -2:
        if get_balance_f(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    return node

def insert(node: TreeNode, key):
    if node is None:
        return TreeNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return balance(node)

def findMin(node: TreeNode):
    if node.left is not None:
        return findMin(node.left)
    else:
        return node

def delete_min(node: TreeNode):
    if node.left is None:
        return node.right
    node.left = delete_min(node.left)
    return balance(node)

def delete(node:TreeNode, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    ###
    else:
        left_node = node.left
        right_node = node.right
        if right_node is None:
            return left_node
        min_node = findMin(right_node)
        min_node.right = delete_min(right_node)
        min_node.left = left_node
        return balance(min_node)
    return balance(node)

def search(node: TreeNode, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


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
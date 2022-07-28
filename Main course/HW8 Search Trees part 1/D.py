import sys
SEPARATOR = "\n"
UNICODE = "utf-8"
DIVIDER = 10 ** 9
MAX = sys.maxsize
MIN = -(sys.maxsize - 1)


class TreeNode():
    """Node for avl tree"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.min = key
        self.max = key
        self.sum = 0


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
    update_min_max(node)
    update_sum(node)
    fixheight(q)
    update_min_max(q)
    update_sum(q)
    return q


def rotate_left(node: TreeNode):
    p = node.right
    node.right = p.left
    p.left = node
    fixheight(node)
    update_min_max(node)
    update_sum(node)
    fixheight(p)
    update_min_max(p)
    update_sum(p)
    return p


def balance(node: TreeNode):
    fixheight(node)
    update_min_max(node)
    update_sum(node)
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
        update_min_max(node)
        update_sum(node)
    elif key > node.key:
        node.right = insert(node.right, key)
        update_min_max(node)
        update_sum(node)
    return balance(node)


def get_sum(node: TreeNode):
    if node is not None:
        return node.sum
    else:
        return 0


def get_max(node: TreeNode):
    if node is not None:
        return node.max
    else:
        return MIN


def get_min(node: TreeNode):
    if node is not None:
        return node.min
    else:
        return MAX


def update_min_max(node: TreeNode):
    node.min = min(get_min(node.left), get_min(node.right), node.key)
    node.max = max(get_max(node.left), get_max(node.right), node.key)


def update_sum(node: TreeNode):
    node.sum = get_sum(node.left) + get_sum(node.right)
    if node.left is not None:
        node.sum += node.left.key
    if node.right is not None:
        node.sum += node.right.key


def sum_tree(node: TreeNode, l, r):
    if node is None:
        return 0
    if node.key > r:
        return sum_tree(node.left, l, r)
    if node.key < l:
        return sum_tree(node.right, l, r)
    if node.left is None and node.right is None:
        return node.key
    if node.min >= l and node.max <= r:
        return node.sum + node.key
    return sum_tree(node.left, l, r) + sum_tree(node.right, l, r) + node.key


############ ---- Main Block ---- ############

def solve():

    data = sys.stdin.buffer.readlines()

    result_list = []
    n_operations = len(data)
    root = None
    prev = '+'

    for i in range(n_operations):
        if i == 0:
            continue

        command = str(data[i].decode(UNICODE))[:-1].split()

        if command[0] == "+":
            if prev == '+':
                root = insert(root, int(command[1]))
            else:
                root = insert(root, (int(command[1]) + res) % DIVIDER)

        elif command[0] == "?":
            res = sum_tree(root, int(command[1]), int(command[2]))
            result_list.append(str(res))

        prev = command[0]

    encoded_array = (SEPARATOR.join(result_list)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)


if __name__ == "__main__":
    solve()
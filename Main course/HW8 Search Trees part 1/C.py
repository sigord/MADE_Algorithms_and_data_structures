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
        self.size = 1

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
    update_size(node)
    fixheight(q)
    update_size(q)
    return q

def rotate_left(node: TreeNode):
    p = node.right
    node.right = p.left
    p.left = node
    fixheight(node)
    update_size(node)
    fixheight(p)
    update_size(p)
    return p

def balance(node: TreeNode):
    fixheight(node)
    update_size(node)
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
        update_size(node)
    elif key > node.key:
        node.right = insert(node.right, key)
        update_size(node)
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
        update_size(node)
    elif key > node.key:
        node.right = delete(node.right, key)
        update_size(node)
    ###
    else:
        left_node = node.left
        right_node = node.right
        if right_node is None:
            return left_node
        min_node = findMin(right_node)
        update_size(min_node)
        min_node.right = delete_min(right_node)
        update_size(min_node)
        min_node.left = left_node
        update_size(min_node)
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

def size(node: TreeNode):
    if node is None:
        return 0
    else:
        return node.size

def update_size(node: TreeNode):
    if node is not None:
        node.size = 1 + size(node.left) + size(node.right)

def findKMAX(node: TreeNode, k):
    leftsize = size(node.left)
    if (leftsize == k):
        return node.key
    elif leftsize > k:
        return findKMAX(node.left, k)
    else:
        k -= leftsize + 1
        return findKMAX(node.right, k)



############ ---- Main Block ---- ############

def solve():

    data = sys.stdin.buffer.readlines()
    result_list = []
    n_operations = len(data)
    root = None
    lenght_t = 0
    for i in range(n_operations):
        if i == 0:
            continue

        command = str(data[i].decode(UNICODE))[:-1].split()

        if command[0] == "+1" or command[0] == "1":
            root = insert(root, int(command[1]))
            lenght_t += 1
        elif command[0] == "-1":
            root = delete(root, int(command[1]))
            lenght_t -= 1
        elif command[0] == "0":
            result_list.append(str(findKMAX(root, (lenght_t - int(command[1])))))

    encoded_array = (SEPARATOR.join(result_list)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)


if __name__ == "__main__":
    solve()
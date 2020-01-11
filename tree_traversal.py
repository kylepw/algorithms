from collections import defaultdict, deque

"""Tree traversal examples."""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        if not self.val:
            return f'Node({self.val})'
        return f'Node({self.val})'


# DFS

def inorder_traverse_re(root):
    """Inorder traversal (recursive)."""
    values = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        values.append(node.val)
        traverse(node.right)

    traverse(root)

    return values

def inorder_traverse_iter(root):
    """In-order traversal (iterative)."""
    stack = []
    values = []
    current = root

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            values.append(current.val)
            current = current.right
        else:
            break

    return values

def postorder_traverse_re(root):
    """Post-order traversal (recursive)."""
    values = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        values.append(node.val)

    traverse(root)

    return values

def postorder_traverse_iter(root):
    """Post-order traversal (iterative)."""
    stack = [root]
    values = []
    visited = []

    while stack:
        current = stack.pop()
        if current:
            if current not in visited:
                visited.append(current)
            stack.append(current.left)
            stack.append(current.right)
    values = [n.val for n in visited]
    values.reverse()
    return values

def is_symmetric_re(root: TreeNode) -> bool:
    """Check if a binary tree is a mirror of itself (symmetric around its center)."""
    if not root:
        return False

    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    return is_mirror(root, root)

def is_symmetric_iter(root: TreeNode) -> bool:
    """ Check if binary tree is symmetric (iterative)."""
    if not root:
        return False

    q = deque()
    q.appendleft(root)
    q.appendleft(root)
    while q:
        t1 = q.pop()
        t2 = q.pop()

        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        q.appendleft(t1.left)
        q.appendleft(t2.right)
        q.appendleft(t1.right)
        q.appendleft(t2.left)

    return True

# BTS

def bts_level_order(root):
    """Print tree values by level, grouped in lists."""
    if not root:
        return []
    q = deque()
    q.appendleft(root)
    levels = defaultdict(list)
    levels[root] = 0
    result = []

    while q:
        current = q.pop()
        if current:
            if current.left:
                q.appendleft(current.left)
                levels[current.left] = levels[current] + 1
            if current.right:
                q.appendleft(current.right)
                levels[current.right] = levels[current] + 1
    result = [[] for _ in range(len(set(levels.values())))]
    for node, level in levels.items():
        result[level].append(node.val)

    return result


if __name__ == '__main__':
    # DFS
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(4)
    assert inorder_traverse_re(t) == [1, 3, 2, 4]
    assert inorder_traverse_iter(t) == [1, 3, 2, 4]

    assert postorder_traverse_re(t) == [3, 4, 2, 1]
    assert postorder_traverse_iter(t) == [3, 4, 2, 1]

    # [1,2,2,3,4,4,3]
    e = TreeNode(1)
    e.left = TreeNode(2)
    e.right = TreeNode(2)
    e.left.left = TreeNode(3)
    e.left.right = TreeNode(4)
    e.right.left = TreeNode(4)
    e.right.right = TreeNode(3)

    assert is_symmetric_re(e) is True
    assert is_symmetric_iter(e) is True

    # BTS
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    p.left.right = TreeNode(5)
    assert bts_level_order(p) == [[1],[2,3],[4,5]]

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.left.left = TreeNode(3)
    q.left.left.left = TreeNode(4)
    q.left.left.left.left = TreeNode(5)
    assert bts_level_order(q) == [[1], [2], [3], [4], [5]]


    def has_path_sum(root: TreeNode, sum: int) -> bool:
        """

        Determine if the tree has a root-to-leaf path such that adding up
        all the values along the path equals the given sum.

        Ex:
            return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return has_path_sum(root.left, sum) or has_path_sum(root.right, sum)

    # [5,4,8,11,null,13,4,7,2,null,null,null,1], 22
    g = TreeNode(5)
    g.left = TreeNode(4)
    g.right = TreeNode(8)
    g.left.left = TreeNode(11)
    g.right.left = TreeNode(13)
    g.right.right = TreeNode(4)

    # [1, 2]
    h = TreeNode(1)
    h.left = TreeNode(2)

    #print(hasPathSum(g, 22))
    print(has_path_sum(h, 2))



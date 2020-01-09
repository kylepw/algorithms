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

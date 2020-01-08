"""Tree traversal examples."""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        if not self.val:
            return f'Node({self.val})'
        return f'Node({self.left.val if self.left else None}) <- NODE({self.val}) -> Node({self.right.val if self.right else None})'


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




if __name__ == '__main__':
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(4)
    assert inorder_traverse_re(t) == [1, 3, 2, 4]
    assert inorder_traverse_iter(t) == [1, 3, 2, 4]

    assert postorder_traverse_re(t) == [3, 4, 2, 1]
    assert postorder_traverse_iter(t) == [3, 4, 2, 1]

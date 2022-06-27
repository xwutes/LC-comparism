# LC_104  maximum depth of binary tree
def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# ----------------- iterative way using BFS -------------------
import collections


def iter_maxDepth(root):
    if not root:
        return 0
    q = collections.deque([root])
    level = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

    return level
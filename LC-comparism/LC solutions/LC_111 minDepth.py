# LC_111 minDepth
import collections
class TreeNode:
    def __init__(self,val = 0, left = None, right =None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def minDepth(self, root:TreeNode)->int:

        if not root:
            return 0

        q = collections.deque()
        q.append((root, 1))

        while q:
            node, depth = q.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                q.qppend((node.left, depth + 1))

            if node.right:
                q.qppend((node.right, depth + 1))
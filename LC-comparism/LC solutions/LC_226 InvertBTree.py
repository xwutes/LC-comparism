# LC_226 InvertBTree
# Definition for a binary tree node.
from matplotlib import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        q = collections.deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                                                # swapping the pointer at this spot 
                if node.left:
                    q.append(node.left)         # almost same handling interms of append method
                if node.right:
                    q.append(node.right)

        return root                             # the output should be an entire treenode, no counting involves

# ------------------------- recursion way ----------------
# this approach consumes much more RAM than the previous one.
def invertTree(self, root: TreeNode) -> TreeNode:

    if not root:
        return None
    
    left = invertTree(root.left)            # recursion postion that function on tree left
    right = invertTree(root.right)

    root.right, root.left = left,right      # swap the value assigned before

    return root


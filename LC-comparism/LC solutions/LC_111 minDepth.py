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
        q.append((root, 1))                         # main difference here is we are passing a tuple 

        while q:
            node, depth = q.popleft()
                                                    # we could see no for loop here like traversing level
            if not node.left and not node.right:    
                return depth                        # where the loop ends

            if node.left:
                q.qppend((node.left, depth + 1))    # passing two arguments at the same time

            if node.right:
                q.qppend((node.right, depth + 1))
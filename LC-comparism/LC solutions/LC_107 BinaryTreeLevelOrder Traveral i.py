# LC_107 BinaryTreeLevelOrder Traveral ii
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import Optional
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()
        q.append(root)
        res = collections.deque()           # list adding from beginning will take O(n)
        while q:
            
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.appendleft(level)           # deque() appendleft will take O(1)
                    
        return res 
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
        # res = []           
        while q:
            
            level = []
            for i in range(len(q)):         # this cycle is looping in level,
                node = q.popleft()          # only if there still have node in this level
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # if indent here for res.append, there will be redundance of the result
            res.appendleft(level)           # deque() appendleft will take O(1)
            #res.append(level)                                # indentation is really important for this case
        return res
        #return res[::-1] 
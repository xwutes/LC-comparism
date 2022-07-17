#LC_103 Binary Tree Zigzag Level Order Traversal

#Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        f = True
        res = []
        
        while q:
            level = collections.deque()
            for _ in range(len(q)):
                node = q.popleft()
                if f:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            f = not f 
            res.append(list(level))
            
        return res

# ------------------------------- another solution ----------------------------------
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    
    q = collections.deque([root])
    f = True
    res = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if f:
            level = level[::-1]
        res.append(level)
        f = not f

    return res

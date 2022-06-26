# LC_102 BinaryTreeLevelOrder Traversal levelOrder
import collections

class TreeNode:
    def __int__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def levelOrder(self, root: TreeNode):
#         if root is None:
#             return []
#         res = []
#         q = [root]
#         while q:
#             res.append([node.val for node in q])
#             q = [kid for node in q for kid in (node.left, node.right) if kid]
#         return res

#------------------------antoher clear approach ----------------------
def levelOrder(root):

    res = []
    q = collections.deque()
    q.append(root)

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res

root = [3,9,20,None,None,15,7]
# expected output:[[3],[9,20],[15,7]]
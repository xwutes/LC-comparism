# LC_144 binary tree preorder traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if root == None:
            return res
        
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        # 回溯算法思路
        res = []

        def traverse(node):
            if node == None:
                return
            # 前序遍历位置
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return res
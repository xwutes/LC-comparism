# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q1 = collections.deque([root])
        q2 = collections.deque([root])

        while q1 or q2:
            s1, s2 = len(q1), len(q2)
            if s1 != s2:
                return False

            for _ in range(s1):
                node1, node2= q1.popleft(), q2.popleft()
                if not node1 and not node2:           # condition always before loop operation
                    continue                          # notice here we don't return False
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                q1.append(node1.left)                 # loop operation that varies
                q1.append(node1.right)

                q2.append(node2.right)
                q2.append(node2.left)

        return True        
# @lc code=end


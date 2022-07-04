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
                return depth                        # where the loop ends, return depth not break

            if node.left:
                q.qppend((node.left, depth + 1))    # passing two arguments at the same time

            if node.right:
                q.qppend((node.right, depth + 1))


#-------------------------- Standard BFS approach ---------------------
def minDepth(self, root:TreeNode):
    if not root:
        return None
    depth = 1
    q = [root]

    while q:
        for i in range(len(q)):
            node = q.pop(0)
            if node.left is None and node.right is None:
                return depth                        # all implementation is return depth not break
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1                                  # depth plus one in python(behind if) is different in java(before if)
    return depth                                    # for loops ends by the first node 3 then depth initial changed from 1 to 2
            



#-------------------------- BFS ---------------------------------

def minDepth(self, root:TreeNode):
    to_visit = collections.deque([(root,1)])

    while to_visit:
        node, ct = to_visit.popleft()
        if not node:
            continue
        if not node.left and not node.right:
            return ct
        to_visit += [(node.left, ct + 1),(node.right, ct + 1)]

    return 0


#---------------------------BFS without input a tuple ------------

def minDepth(self, root:TreeNode):
    if not root:
        return 0
    stack = [root]
    level = 1
    while stack:
        for node in stack:                                  # condition judgement putting here
            if not node.left and not node.right:            
                return level                                # without setting break, when condition met, while loop stop
        level += 1
        stack = [child for node in stack for child in (node.left, node.right) if child]
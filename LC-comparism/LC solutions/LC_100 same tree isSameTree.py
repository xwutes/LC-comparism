# LC_100 same tree isSameTree
def isSameTree(self, p, q):
    # 判断一对节点是否相同

    if p == None and q == None:
        return True
    if p == None or q == None or p.val != q.val:
        return False

                                                        #[10,5,15] and [10,5,null,null,15] 
        return False
    # 判断其他节点是否相同
    return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
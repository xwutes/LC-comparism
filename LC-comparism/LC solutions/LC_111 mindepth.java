// LC_111 Minimum Depth of Binary Tree
class Solution{
    public int minDepth(TreeNode root) {
        int depth = 0;
        if(root == null) 
        return depth;
    }
    Queue<TreeNode> queue = new ArrayDeque<TreeNode>();
    queue.offer(root);
    loop:while(!queue.isEmpty()){
        int size = queue.size();
        for(int i = 0; i < size; i++){
            TreeNode node = queue.poll();
            if(node.left == null && node.right == null){
                break loop;
            }
            if(node.left != null)
                queue.offer(node.left);
            if(node.right != null)
                queue.offer(node.right);
        }    
    }
    return depth;
}

// ------------------------- other approach -------------------------

class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        // root 本身就是一层，depth 初始化为 1
        int depth = 1;

        while (!q.isEmpty()) {
            int sz = q.size();
            /* 遍历当前层的节点 */
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                /* 判断是否到达叶子结点 */
                if (cur.left == null && cur.right == null)
                    return depth;
                /* 将下一层节点加入队列 */
                if (cur.left != null)
                    q.offer(cur.left);
                if (cur.right != null)
                    q.offer(cur.right);
            }
            /* 这里增加步数 */
            depth++;
        }
        return depth;
    }
}
// 详细解析参见：
// https://labuladong.github.io/article/?qno=111

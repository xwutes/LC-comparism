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

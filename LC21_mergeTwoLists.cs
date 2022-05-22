static Node Zip(Node p, Node q){
    Node head = new Node(), zipper = head;
    while (p!= null && q!= null){
        if(p.val <= q.val){
            zipper.next = p;
            p = p.next;
        }else{
            zipper.next = q;
            q = q.next;
        }
        zipper = zipper.next;
    }

    zipper.next = p ?? q;
    return head.next;
}
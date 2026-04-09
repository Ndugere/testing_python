from collections import deque

def same_tree(p_root, q_root):
    if not p_root and not q_root:
        return True 
    if not p_root or not q_root:
        return False
    
    queue_p = deque([p_root])
    queue_q = deque([q_root])

    while queue_p and queue_q:
        p_node = queue_p.popleft()
        q_node = queue_q.popleft()
        if p_node.data != q_node.data:
            return False
        if (q_node.left and not p_node.left) or (p_node.left and not q_node.left):
            return False
        elif q_node.left and p_node.left:
            queue_p.append(p_node.left)
            queue_q.append(q_node.left)
        if (q_node.right and not p_node.right) or (p_node.right and not q_node.right):
            return False
        elif q_node.right and p_node.right:
            queue_p.append(p_node.right)
            queue_q.append(q_node.right)
    
    return not queue_q and not queue_p




        
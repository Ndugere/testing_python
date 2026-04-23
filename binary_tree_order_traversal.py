from collections import deque

def binary_tree_order_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    res = []
    
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            res.append(node.data)
            
            for child in (node.left, node.right):
                if child:
                    queue.append(child)
    
    return res
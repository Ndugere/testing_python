from collections import deque

def path_sum(root, target):
    if not root:
        return False
    
    stack = [(root, root.data)]
    
    while stack:
        node, curr_sum = stack.pop()
        
        # Check leaf node
        if not node.left and not node.right and curr_sum == target:
            return True
        
        if node.right:
            stack.append((node.right, curr_sum + node.right.data))
        if node.left:
            stack.append((node.left, curr_sum + node.left.data))
    
    return False

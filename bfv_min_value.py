from collections import deque

def bfv_min_value(root):

    if root is None:
        return None
    
    queue = deque([root])
    min_value = float("inf")

    while queue:
        current = queue.popleft()

        if current.val < min_value:
            min_value = current.val
        
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
        
    return min_value


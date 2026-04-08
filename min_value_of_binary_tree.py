from collections import deque

def min_value_of_binary_tree(root):
    if not root:
        return float("inf")
    
    queue = deque([root])
    min_value = float("inf")
    while queue:
        min_at_level = float("inf")
        for _ in range(len(queue)):
            node = queue.popleft()
            min_at_level = min(node.data, min_at_level)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        min_value = min(min_at_level, min_value)
    return min_value
        
        
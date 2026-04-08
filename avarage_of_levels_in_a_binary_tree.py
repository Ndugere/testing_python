from collections import deque

def average_of_levels_in_binary_tree(root):
    if not root:
        return []
    queue = deque([root])
    averages = []

    while queue:
        level_values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_values.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        averages.append(sum(level_values) / len(level_values))
    
    return averages

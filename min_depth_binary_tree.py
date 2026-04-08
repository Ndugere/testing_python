from collections import deque

def minimum_depth_binary_tree(root):
    if not root:
        return 0
    
    queue = deque([root])
    depth = 1

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
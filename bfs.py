from collections import deque


def bfs(root, value):

    if root is None:
        return False
    
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.val == value:
            return True
        
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return False

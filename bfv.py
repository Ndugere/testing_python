from collections import deque

def bfv(root):
    res = []

    if root is None:
        return res
    
    queue = deque([root])


    while queue:
        current = queue.popleft()

        res.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return res

from collections import deque

def bfv_tree_sum(root):

    res = 0

    if root is None:
        return res
    

    queue = deque([root])


    while queue:

        current = queue.popleft()

        res += int(current.val)

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)

    return res 
def dfv_min_value(root):

    if root is None:
        return None
    
    stack = [root]

    min_value = float("inf")

    while stack:
        current = stack.pop()

        if current.val < min_value:
            min_value = current.val
        
        if current.right:
            stack.append(current.right)
        
        if current.left:
            stack.append(current.left)

    return min_value
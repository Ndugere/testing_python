def dfv_tree_sum(root):

    res = 0

    if root is None:
        return res 
    
    stack = [root]

    while stack:
        current = stack.pop()
        res += int(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return res

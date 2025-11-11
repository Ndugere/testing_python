def dfv(root):

    if root is None:
        return 
    
    stack = [root]

    res = []

    while stack:

        current = stack.pop()

        res.append(current.val)

        

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    return res
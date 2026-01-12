def dfs(root, value):

    if root is None:
        return False
    
    stack = [root]

    while stack:
        current = stack.pop()

        if current.val == value:
            return True
        
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return False


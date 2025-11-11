def dfv_recur(root):
    if root is None:
        return []
    
    res = [root.val]
    
    left_values = dfv_recur(root.left)
    right_values = dfv_recur(root.right)

    res.extend(left_values)
    res.extend(right_values)

    return res

def max_root_to_leaf_sum(root):

    if root is None:
        return float("-inf")
    
    if root.left is None and root.right is None:
        return root.val
    
    max_child_value = max(
        max_root_to_leaf_sum(root.left),
        max_root_to_leaf_sum(root.right)
    )

    return root.val + max_child_value

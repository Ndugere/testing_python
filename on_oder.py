def on_o_traversal(root):
    if root is None:
        return []
    res = []
    res.extend(on_o_traversal(root.left))
    res.append(root.data)
    res.extend(on_o_traversal(root.right))

    return res


def is_same_tree(p, q):
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        if not node1 or not node2 or node1.data != node2.data:
            return False
        stack.append((node1.right, node2.right))
        stack.append((node1.left, node2.left))
    return True

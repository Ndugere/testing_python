def dfv_recur_acc(root, res=None):
    if res is None:
        res = []

    if root is None:
        return res

    res.append(root.val)
    dfv_recur_acc(root.left, res)
    dfv_recur_acc(root.right, res)

    return res

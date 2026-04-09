from collections import deque
from typing import List, Optional

class Node:
    def __init__(self, data: int, left: Optional['Node']=None, right: Optional['Node']=None):
        self.data = data
        self.left = left
        self.right = right

def level_order_traversal(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level_items = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_items.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_items)
    return result

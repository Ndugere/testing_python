from collections import deque
from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if not image or not image[0]:
        return image
    
    color_to_change = image[sr][sc]
    if color_to_change == newColor:
        return image
    
    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = newColor
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == color_to_change:
                image[nr][nc] = newColor
                queue.append((nr, nc))
    
    return image

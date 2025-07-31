import math

class Vec2d:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")

    def __add__(self, other):
        if isinstance(other, Vec2d):
            return Vec2d(self.x + other.x, self.y + other.y)
        return None

    def __sub__(self, other):
        if isinstance(other, Vec2d):
            return Vec2d(self.x - other.x, self.y - other.y)
        return None

    def __repr__(self):
        return f"Vec2d(x={self.x}, y={self.y})"

def iso_to_screen_staggered(mapX, mapY, logicTileWidth, logicTileHeight,
                            camera_offset_x=0, camera_offset_y=0):
    base_screenX = mapX * logicTileWidth
    base_screenY = mapY * (logicTileHeight / 2)

    currentRow = int(mapY)
    row_offset = logicTileWidth / 2 if (currentRow % 2 != 0) else 0

    screenX = base_screenX + row_offset - camera_offset_x
    screenY = base_screenY - camera_offset_y

    return screenX, screenY

def findFirstPixelY(surface):
    width, height = surface.get_size()
    for y in range(height):
        for x in range(width):
            if surface.get_at((x, y))[3] > 0:
                return y
    return height

def findFirstPixelX(surface):
    width, height = surface.get_size()
    for x in range(width):
        for y in range(height):
            if surface.get_at((x, y))[3] > 0:
                return x
    return width

def findLastPixelY(surface):
    width, height = surface.get_size()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if surface.get_at((x, y))[3] > 0:
                return y


def findLastPixelX(surface):
    width, height = surface.get_size()
    for x in range(width - 1, -1, -1):
        for y in range(height):
            if surface.get_at((x, y))[3] > 0:
                return x

def distance(start, end):
    return ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5

delta = 0.25

def distanceToLine(start, end, point):
    x1, y1 = start
    x2, y2 = end
    x0, y0 = point
    numerator = abs((y2 - y1)*x0 - (x2 - x1)*y0 + x2*y1 - y2*x1)
    denominator = math.hypot(y2 - y1, x2 - x1)
    return numerator / denominator if denominator != 0 else float('inf')

def pointOnLine(start, end, point):
    if not(min(start[0], end[0]) <= point[0] <= max(start[0], end[0])
           and min(start[1], end[1]) <= point[1] <= max(start[1], end[1])):
        return False
    return distanceToLine(start, end, point) < delta


import queue

def bfs(start, end, blockers):
    start = (int(start[0] + 0.5), int(start[1] + 0.5))
    end = (int(end[0] + 0.5), int(end[1] + 0.5))
    q = queue.Queue()
    q.put(start)
    visited = set()
    visited.add(start)
    parent = {start: None}

    while not q.empty():
        current = q.get()
        if current == end:
            path = []
            while parent[current] is not None:
                path.append((current[0] - parent[current][0], current[1] - parent[current][1]))
                current = parent[current]
            return path[::-1]


        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if not(0 <= neighbor[0] < 50 and 0 <= neighbor[1] < 50):
                continue
            if neighbor not in visited and neighbor not in blockers:
                q.put(neighbor)
                parent[neighbor] = current
                visited.add(neighbor)

    return None
import math


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

def pointOnLine(start, end, point):
    if not(min(start[0], end[0]) <= point[0] <= max(start[0], end[0])
           and min(start[1], end[1]) <= point[1] <= max(start[1], end[1])):
        return False
    x1, y1 = start
    x2, y2 = end
    x0, y0 = point
    numerator = abs((y2 - y1)*x0 - (x2 - x1)*y0 + x2*y1 - y2*x1)
    denominator = math.hypot(y2 - y1, x2 - x1)
    dist = numerator / denominator if denominator != 0 else float('inf')
    print(dist)
    return dist < delta
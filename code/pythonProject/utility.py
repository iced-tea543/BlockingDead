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
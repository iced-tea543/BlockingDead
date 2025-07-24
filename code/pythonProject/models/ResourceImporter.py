import csv
import xml.etree.ElementTree as ET

def loadMapFromCSV(filepath):
    mapData = []
    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            parsedRow = []
            for item in row:
                try:
                    parsedRow.append(int(item))
                except ValueError:
                    pass
            if parsedRow:
                mapData.append(parsedRow)
    return mapData


def loadTSX(filePath):
    tree = ET.parse(filePath)
    root = tree.getroot()

    tileData = {}
    for tile in root.findall("tile"):
        tileID = int(tile.attrib["id"])
        image = tile.find("image")
        source = image.attrib["source"] if image is not None else None
        tileData[tileID] = source

    return tileData


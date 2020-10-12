import os

SEGMENTS = {
    "Equity": "EQ",
    "Future & Options": "NSE-FO",
    "Currency": "NSE-CDS",
    "Commodity": "MCX-COM",
    "Mutual Funds": "MF",
    "Equity (External trades)": "EQX",
    "MF (External trades)": "MFX",
}


def getOutputPath(folder, fileName):
    return os.path.join(folder, fileName)


def readProperties():
    import json
    with open("properties.json") as properties:
        return json.load(properties)


def isDirectoryExists(path):
    return os.path.exists(path)


def createDirectory(path):
    os.makedirs(path)

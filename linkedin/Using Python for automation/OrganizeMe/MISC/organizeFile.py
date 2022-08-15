import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENT": [".pdf", ".rtf", ".txt"],
    "AUDIO": [".mp3", ".m4a", ".m4b"],
    "VIDEOS": [".mp4", ".avi", ".mov"],
    "IMAGES": [".jpg", ".jpeg", ".png"]
}
def pickDir(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

def organizeDir():
    for item in os.scandir():
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        print(filePath, fileType, directory)
        filePath.rename(directoryPath.joinpath(filePath))
organizeDir()
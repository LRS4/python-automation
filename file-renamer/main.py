#/usr/bin/python3
from renamer import FileRenamer

if __name__ == "__main__":
    folderPath, text, replaceWith, extension = FileRenamer.start()  
    fr = FileRenamer(folderPath, text, replaceWith, extension)
    fr.rename_files()  

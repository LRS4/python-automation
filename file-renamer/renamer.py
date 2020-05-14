#/usr/bin/python3
import os
import pyfiglet

class FileRenamer:
    def __init__(self, folderPath, text, replaceWith, extension):
        self.folderPath = folderPath
        self.text = text
        self.replaceWith = replaceWith
        self.extension = extension

    def rename_files(self):
        try:
            os.chdir(self.folderPath)
            count = 0
            for file in os.listdir():
                name, extension = os.path.splitext(file)
                if self.text in name:
                    new_name = name.replace(self.text, self.replaceWith)
                    if self.extension == "":
                        os.rename(file, new_name + extension)
                    else:
                        os.rename(file, new_name + self.extension)
                    count += 1
                else:
                    print(f'"{self.text}" not in filename "{name}"')
        except(FileNotFoundError):
            print("Invalid folder path entered!")

        self.finish(self.folderPath, count)

    @staticmethod
    def start():
        ascii_banner = pyfiglet.figlet_format("Bulk File Renamer")
        print(ascii_banner)
        folderPath = input("Folder path: ")
        text = input("Find text: ")
        replaceWith = input("Replace with: ")
        change_extension = input("Amend file types? (Y/N) ", )
        if change_extension == "Y" or change_extension == "y":
            extension = input('New file extension: ')
            if not extension.startswith("."):
                raise ValueError('Not a valid file extension. Must start with "."')
        else:
            extension = ""
        return folderPath, text, replaceWith, extension

    def finish(self, folderPath, filesCount):
        print("Done!", end="\n")
        print(f"{filesCount} files in folder {folderPath} were renamed.")

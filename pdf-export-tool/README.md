# PDF Export Tool

## Purpose
* The tool at present:
* Reads table in excel sheet
* Creates unique folders in a directory
* Enters search term into Power BI Report dropdown slicer
* Exports report to PDF
* Saves the PDF to chosen file path
* Repeats above steps for each line in excel sheet table

## Packages Used

* [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/)
* [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
* [PyWin32 (Repo)](https://github.com/mhammond/pywin32)
* [PyWin32 (Documentation)](http://timgolden.me.uk/pywin32-docs/)
* [OS](https://docs.python.org/3/library/os.html?highlight=osmakedirs#os.makedirs)

## Prerequisites

* [Visual Studio Code (VS Code)](https://code.visualstudio.com/download)
* [Anaconda distibution with Python 3.7](https://docs.anaconda.com/anaconda/install/windows/)
* VS Code Extensions:
* Anaconda Extension
* Code Runner
* [Information on installing extensions](https://code.visualstudio.com/docs/editor/extension-gallery)

## Start

* Open Anaconda Prompt
* Navigate to project directory
* Run "pip install -r requirements.txt"
* Run program in VS Code using F1 then 'Run Python File in Terminal'
* Open and switch to the Power BI Desktop window
* The program will then take over and execute the script until finished

## Changing the program

* The main changes required are:
* Changing the excel file input variables
* Changing the screen resolution parameters for desktop and/or laptop - current screen resolution can be found in Display Settings or at sites like [What Is My Screen Resolution](http://whatismyscreenresolution.net/)
* Changing the screen coordinates for clicks (you can locate screen coordinates for clicks by running screen_coordinates.py which will show X Y coordinates of the cursor position)
* Changing what the program types into filters etc.
* Changing the output path

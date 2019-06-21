#!python3
""" a script to launch some commonly used programs """
import os
import sys
import time
import random
import subprocess
import pyautogui

def main():
	start = time.time()

	# start chrome
	os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
	print("Chrome started..")
	time.sleep(2)
	
	# start vs code full screen
	os.popen("code")
	time.sleep(2)
	pyautogui.hotkey('alt', 'space')
	pyautogui.typewrite(['down','down','down','down','down','enter'])
	print("VS Code started..")
	time.sleep(2)
	
	# open dropbox folder
	os.startfile(r"C:\Users\L.Spencer\Dropbox")
	print("Dropbox started..")
	
	# exit program
	print("Done.")
	end = time.time()
	print("Total run time: " + str(end - start))

	# random quote file split on double \n
	file = open("quotes.txt","r", encoding='utf-8')
	reader = file.read()
	quotes = reader.split("\n\n")
	x = random.randint(0,(len(quotes)-1))
	print()
	print(quotes[x])
	file.close()
	time.sleep(30)
	sys.exit("Have a nice day!")
	
if __name__ == "__main__":
	main()

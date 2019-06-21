#!python3
""" a script to import images from camera to a new folder """
import os
import sys
import time
import shutil

def main():

	# start timer
	print("Program started..")
	start = time.time()
	
	# if less than three arguments exit
	if len(sys.argv) != 4:
        sys.exit("Usage: python auto-cam-importer.py location month yyyy")
    else:
        folder = sys.argv[1].capitalize()
		month = sys.argv[2].capitalize()
		year = sys.argv[3]

	folder_name = str(folder + " (" + month + " " + year + ")")
		
	# check camera dcim directory exists
	for i in range(5):
		dcim = os.path.isdir("/home/el")
		if dcim == False:
			print("DCIM not found.")
			print("Searching again..")
			time.sleep(5)
		else:
			print("DCIM found!")
	
	# final dir check
	if dcim == False:
		sys.exit("Unable to locate DCIM folder")
	
	# copy contents into new folder
	print("Copying images..")
	#shutil.copytree(SOURCE, DESTINATION)
	
	# or create new folder and open it
	#os.mkdir(folder_name)
	
	# open folder to view copied files
	print("Opening folder..")
	#os.startfile(r"Cam folder")
	print("Program done")
	
	# print run time
	end = time.time()
	print("Total run time: " + str(end - start))
	
	
if __name__ == "__main__":
	main()
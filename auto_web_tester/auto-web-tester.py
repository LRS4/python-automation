#! python3.
""" A program to automate web form testing """
import os
import random
import time
import webbrowser
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from json import dumps


def main():
	""" Completes the online form """
	# initialise timer
	start = time.time()
	print("Program started...")
	
	# open web browser with selenium
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")

	driver = webdriver.Chrome("C:\\Users\\L.Spencer\\Documents\\Webdriver\\chromedriver.exe", chrome_options=options)
	driver.get("https://ml-titanic-app.herokuapp.com")		

	# set number of testing cycles 
	for i in range(1):
			
		# initialise male or female user, create name and title
		print("Generating random user details... ", end="")
		MF = random.randint(0, 1)
		if MF == 1:
			name = male_name() + " " + surname()
		else:
			name = female_name() + " " + surname()
		print(name)
		
		# wait until start button element is clickable
		try:
			startBtn = wait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'nextOne')))
			startBtn.click()
			print("Clicking start...")
		except TimeoutException:
			print("Waiting for start button...")

		# complete name section
		print("Completing name...")
		driver.find_element_by_id("fullName").send_keys(name)
		driver.find_element_by_id("nextTwo").click()	

		# complete title section
		print("Completing title...")
		randTitle = title(MF)
		driver.execute_script("document.getElementsByName(\"title\")[0].options[" + str(randTitle) + "].selected = true;")
		driver.find_element_by_id("nextThree").click()

		# complete age section
		print("Completing age...")
		randAge = random.randint(1,100)
		driver.find_element_by_id("inputAge").send_keys(randAge)
		driver.find_element_by_id("nextFour").click()

		# complete gender section
		print("Completing gender...")
		if MF == 1:
			driver.execute_script("document.getElementsByName(\"gender\")[0].click();")
		else:

			driver.execute_script("document.getElementsByName(\"gender\")[1].click();")
		driver.find_element_by_id("nextFive").click()

		# complete class section
		print("Completing class...")
		randClass = random.randint(0,2)
		driver.execute_script("document.getElementsByName(\"class\")[" + str(randClass) +"].click();")
		driver.find_element_by_id("nextSix").click()

		# complete family section
		print("Completing family...")
		randFamily = random.randint(0,8)
		driver.find_element_by_id("inputFamily").click()
		pyautogui.typewrite(['\b'])	
		driver.find_element_by_id("inputFamily").send_keys(randFamily)
		driver.find_element_by_id("nextSeven").click()

		# complete completion section
		print("Submitting...")
		time.sleep(10)
		driver.find_element_by_id("submit").click()
		time.sleep(5)

		# restart form
		print("Restarting form...")
		driver.find_element_by_class_name("navbar-brand").click()
		time.sleep(3)

	# close web browser
	driver.quit()
	
	# end timer, print run time
	end = time.time()
	print("Program done!")
	print("Total run time: " + str(round(end - start, 2)) + "s")


def title(mf):
	""" Generates a random M or F title """
	if mf == 1:
		titles = [1,3,4,5,7,8,9,1,11,14]
		title = titles[random.randint(0,(len(titles)-1))]
		return title
	else:
		titles = [2,6,12,13,15,16]
		title = titles[random.randint(0,(len(titles)-1))]
		return title
	
def male_name():
	""" Retrieve a random name """
	file = open("male-first-names.txt")
	reader = file.read()
	names = reader.split()
	name = names[random.randint(0,(len(names)-1))]
	return name.capitalize()
	
def female_name():
	""" Retrieve a random name """
	file = open("female-first-names.txt") 
	reader = file.read()
	names = reader.split()
	name = names[random.randint(0,(len(names)-1))]
	return name.capitalize()
	
def surname():
	""" Retrieve a random surname """
	file = open("common-surnames.txt")
	reader = file.read()
	names = reader.split()
	name = names[random.randint(0,(len(names)-1))]
	return name.capitalize()

	
if __name__ == "__main__":
	main()
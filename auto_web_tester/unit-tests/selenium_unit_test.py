from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome("C:\\Users\\L.Spencer\\Documents\\Webdriver\\chromedriver.exe", chrome_options=options)
driver.get("https://www.google.co.uk") # working
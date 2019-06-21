import webbrowser
url = "https://www.google.co.uk"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url) # working

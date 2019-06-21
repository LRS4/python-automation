"""
A program to scrape a website and extract email addresses and phone numbers using regex
"""

import requests
import re
from bs4 import BeautifulSoup as bs

# scrape html source
source = requests.get("https://www.nottingham.ac.uk/contact/").text
soup = bs(source, "lxml")
soup_string = str(soup)

# create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username - lower, upper, numbers, a dot, percent, plus, or hyphen
    @                      # @ symbol 
    [a-zA-Z0-9.-]+         # domain name - lower, upper, numbers, a dot or hyphen
    (\.[a-zA-Z]{2,4})      # dot-something - lower, upper, between 2 and 4 chars
        )''', re.VERBOSE)

# find all pattern matches
allEmails = emailRegex.findall(soup_string)
print(allEmails)

# create phone regex
phoneRegex = re.compile(r'\d{3}[-\.\s]??\d{4}[-\.\s]??\d{4}|\d{5}[-\.\s]??\d{3}[-\.\s]??\d{3}|(?:\d{4}\)?[\s-]?\d{3}[\s-]?\d{4})') # UK numbers
allNumbers = phoneRegex.findall(soup_string)
print(allNumbers)
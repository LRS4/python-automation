#! python3
""" Regular expressions, called regexes for short, are descriptions for a pattern of text. """

import re

# create a regex pattern for a phone number
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# search for that pattern
mo = phoneNumRegex.search("My mobile number is 444-555-1234")

# return matched results (group)
print("Phone number found: " + mo.group())

# more complex to grab area code and number (groups)
areaNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = areaNumRegex.search("My mobile number is 444-555-1234")
print("Area code: " + mo.group(1) + " Phone number: " + mo.group(2))

# using this or | that
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print("Hero: " + mo1.group())

# using findall to return array - search only returns one result
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
allNumbers = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(allNumbers)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
areaNumbers = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(areaNumbers)

# creating your own regex - for vowels or ^ for not vowels
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vowels)
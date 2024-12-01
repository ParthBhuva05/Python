# Regular Expression in Python


# Regular expressions, or "regx" for short, are a powerful tool for working with strings and text data in python. they allow you to match and manipulate strings based on patterns, making it easy to perform complex strings oprations with jast a few lines of a code.

# Matacharacters in regular expressons

# 1  -  [] ----> Repersent a character class
# 2  -  ^  ----> Matches the beginning
# 3  -  $  ----> Matches the end
# 4  -  .  ----> Matches any character expect newline
# 5  -  ?  ----> Matches zero or one occurrences
# 6  -  |  ----> Means or (Matches with any of the characters)
# 7  -  *  ----> Any number of occurrences(including 0 occurrences)
# 8  -  +  ----> One or more occurrences
# 9  -  {} ----> Indicate number of occurrences of a prceding RE 
# 10 -  {} ----> Enclose a group of REs


# Find list of more meta characters here - https://www.ibm.com/docs/en/rational- clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions


# Importing re Package
# import re


# In Python, regular expressions are supported by the re module. The basic syntax for working with regular expressions in Python is as follows:


# Searching for a pattern in re using re.search() Method

# re.search() method either returns None (if the pattern doesn't match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. We can use research method like this to search for a pattern in regular expression:


# Searching for a pattern in re using re.findall() method

# You can also use the re.findall function to find all occurrences of the pattern in a string.

# import re 
# pattern = r"expression"
# text = "The cat is in the hat."

# matches = re.findall(pattern, text)
# print(matches) 

# Website link :-  https://regexr.com

# Replacing a pattern



import re

pattern = r"[A-Z]+yclon"

text = '''The koala is Cyclon an arboreal plant-eating marsupial native to Australia, recognised Cyclon worldwide as a symbol of the country. Its closest living relatives Cyclon Dyclon are the wombats. It has a stout, tailless body and large head with round, fluffy Dyclon ears and a large, dark nose Dyclon. The koala has a body length of 60 to 85 Cyclon cm (24 to 33 in) and weighs 4 Dyclon to 15 kg (9 to 33 lb). Fur colour ranges from silver grey to chocolate brown.'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    # print(match)
    print(match.span())
    print(text[match.span()[0]: match.span()[1]])








   
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 07:13:22 2025

@author: dawilly
"""

#strings


# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

name_heavstory = '''Hello my name is Elia william mariki
my babe is heavenlight Elia mariki
we are so in love and inseparable for sure no one can make us apart'''
print(name_heavstory)


# String Concatenation
first_name = 'dawilly'
last_name = 'gene'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 


print(len(first_name))  
print(len(last_name))   
print(len(first_name) > len(last_name))
print(len(full_name)) 


# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n


# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o


# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three)
last_three = language[3:6]
print(last_three) # hon

# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings

language = 'Python'
#string[start:stop:step]
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')


## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = "the days of jackal"
print(challenge.capitalize())

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
challenge  = "the days of jackal"
print(challenge.count('a'))
print(challenge.count('a',3,19))
print(challenge.count("ka"))

# endswith(): Checks if a string ends with a specified ending
challenge  = "the days of jackal"
print(challenge.endswith('jackal'))
print(challenge.endswith('om'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge  = "the\tdays\tof\tjackal"
print(challenge.expandtabs())
print(challenge.expandtabs(1))

# find(): Returns the index of first occurrence of substring
challenge = "the days of the jackal"
print(challenge.find('d'))
print(challenge.find('jackal'))

# format()	formats string into nicer output    
first_name = "dawilly";
last_name = "gene";
job = "software engineer";
country = "Tanzania";
sentence = 'I am {} {} . I am a {}. I live in {}.'.format(first_name,last_name,job,country)
print(sentence)


radius = 10
pi = 3.14
area = pi
result = 'The area of a circle with {} is {}'.format(str(radius),str(area))
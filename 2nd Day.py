#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 03:55:20 2025

@author: dawilly
"""

#Variable in Python

first_name = "dawilly"
last_name = "gene"
country = 'Tanzania'
city = 'dodoma'
age = 25
is_married = False
skills = ['Laravel','HTML','CSS','REACT','JS','JAVA','PYTHON']
personal_info = {
  "first_name":"dawilly",
  "last_name" :"gene",
  "country" :'Tanzania',
  "city" :'dodoma'
  }


#printing the value stored in a variables


print('First name:',first_name)
print('Firstname length :',len(first_name))
print('Lastname :',last_name)
print('Lastname length :',len(last_name))
print('Country : ',country)
print('City ',city)
print('Age : ',age)
print('Married',is_married)
print('Skills',skills)
print('Personal Information : ',personal_info)

#declaring multiple variables in one line

first_name , last_name , country , age , is_married = 'dawilly','gene','Tanzania','25',True
print(first_name,last_name,country,age,is_married)
print('First name:',first_name)
print('Firstname length :',len(first_name))
print('Lastname :',last_name)
print('Lastname length :',len(last_name))
print('Country : ',country)
print('Age : ',age)
print('Married',is_married)


#casting: converting one data type to another data type int(),float(),float(),str(),list,set

#int to float 

numb_int = 10
print('numb_int',numb_int)
num_float = float(numb_int)
print('num_float',num_float)

#float to int
gravity = 9.81
print(int(gravity))


#int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

#str to int or float
num_str = '10.753'
num_float = float(num_str)
print('num_float',num_float)
num_int = int(num_float)
print('num_int',int(num_int))

#str to list
first_name = 'dawillygene'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
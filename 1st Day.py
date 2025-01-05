#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 02:48:06 2025

@author: dawilly
"""


print(3+2) #addition(+)
print(3 - 2) #subraction(-)
print(3 * 2) #multiplication
print(3 / 2) #division
print(3 ** 2) #exponential
print(3 % 2) #modulus
print(3 // 2) #Floor division operator


#printing in a single line the results 

print(3+2, end=" ") #addition(+)
print(3 - 2, end=" ") #subraction(-)
print(3 * 2, end=" ") #multiplication
print(3 / 2, end= " ") #division
print(3 ** 2, end=" ") #exponential
print(3 % 2, end=" ") #modulus
print(3 // 2) #Flooe division operator

#another way of archiving the single line results

print(f"{3+1} {3 -2} {3 * 2} {3 / 2} {3 ** 2} {3 % 2} {3 // 2}")


#Talking about multiple lines comment at once 

'''
print(3+2, end=" ") #addition(+)
print(3 - 2, end=" ") #subtraction(-)
print(3 * 2, end=" ") #multiplication
print(3 / 2, end= " ") #division
print(3 ** 2, end=" ") #exponential
print(3 % 2, end=" ") #modulus
print(3 // 2) #Floor division operator
'''


#checking data types

print(type(10)) #integer
print(type(3.14)) #float
print(type(1 + 3j)) #complex
print(type("dawilly gene")) #string
print(type([1,2.23,"heaven",4])) #list
print(type({'university':'UDOM'})) #Dictionary
print(type({9.8,3.14,2.7})) #set
print(type((9.8, 3.14, 2.7)))  #Tuple
print(type(3==3)) #Bool
print(type(3>=3)) #Bool

#array is a collection of items of the same type. Unlike a list, which can hold elements of different types, arrays enforce uniformity

import array

arr = array.array('i',[1,2,3,4,5,6,7,8,9,10])
print(type(arr))



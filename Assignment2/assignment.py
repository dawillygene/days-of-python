#part 1
'''
1. Basic Indexing:
Given the list numbers = [10, 20, 30, 40, 50], what is the value at index 2 '''

numbers = [10, 20, 30, 40, 50]
print(numbers[2]) # 30



'''2. Negative Indexing:
Using the list fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry'], what element is accessedusing the index -1?'''

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[-1]) #elderberry



"""3. Slicing a List:
Given the list colors = ['red', 'green', 'blue', 'yellow', 'orange'], how would you slice the list toget ['green', 'blue', 'yellow']?"""

colors = ['red', 'green', 'blue', 'yellow', 'orange']
print(colors[1:4])



"""4.Slicing with Step:
For the string alphabet = 'abcdefghijklmnopqrstuvwxyz', write a slice expression to get
every third letter starting from index 1.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[1::3]) #behknqtwz


"""5.Slicing a Tuple:
Given the tuple coordinates = (4, 3, 2, 1, 0), how can you extract the sub-tuple (3, 2, 1)?
"""

coordinates = (4, 3, 2, 1, 0)
print(coordinates[1:-1]) 

"""6. Modifying List through Indexing:
Using the list fruits = ['apple', 'banana', 'cherry', 'date'], change the second element to
'blueberry' using indexing."""

fruits = ['apple', 'banana', 'cherry', 'date']
fruits[1]="blueberry"
print(fruits)


"""7. Using Indexing with Strings:
Given the string text = "Python is awesome!", how would you extract the substring"is" using indexing?"""

text = "Python is awesome!"
print(text[7:9])


"""8.Slicing a List from Start to End:
For the list numbers = [1, 2, 3, 4, 5], how would you slice the entire list using a slicenotation?"""

numbers = [1, 2, 3, 4, 5]
print(numbers[:])

"""
9. Slicing with Negative Indices:
Using the list months = ['January', 'February', 'March', 'April', 'May', 'June'], how would you slice the list to get the last three months?"""

months = ['January', 'February', 'March', 'April', 'May', 'June']
print(months[-3:])


""" 10. Combining Indexing and Slicing:
Given the list values = [10, 20, 30, 40, 50], how would you access the second-to-last
element, and how would you slice out the last two elements? """


values = [10, 20, 30, 40, 50]
second_to_last = values[-2]
print("Second-to-last element:", second_to_last)

values = [10, 20, 30, 40, 50]
last_two = values[-2:]
print("Last two elements:", last_two)



#part 02

"""1. Slicing a List of Lists:
Given the list matrix = [[1, 2], [3, 4], [5, 6], [7, 8]], how would you extract a sublist containingonly the second and third inner lists?
 """

matrix = [[1, 2],[3, 4], [5, 6], [7, 8]]
slicedM = matrix[1:3]
print(slicedM)



"""
Advanced Step Slicing:
For the string text = "abcdefghijklmnopqrstuvwxyz", how would you slice the 
stringtogetthe characters starting from index 2 and ending at index 18, with a step of 4?"""

text = "abcdefghijklmnopqrstuvwxyz"
print(text[2:18:4])



"""Slicing with Ellipsis:
Given the 3D list data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]], use slicing and 
ellipsis to extract all the inner lists from the second and third outer lists."""

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]

print(data[1:3])



"""Slicing with None:
How would you use None in slicing to extract a sublist starting from index 2 to the end, and 
every second element after that, from the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]?"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:None:2])





"""
5. Slicing in Reverse:
Given the list letters = ['a', 'b', 'c', 'd', 'e'], write a slice that returns the list in reverseorder, but without using the reversed()
function or list slicing with a negative step."""

letters = ['a', 'b', 'c', 'd', 'e']

# Reverse the list using indexing and list comprehension

reversed_letters = [letters[i] for i in range(len(letters)-1,-1,-1)]
print("Reversed list:", reversed_letters)


print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

letters = ['a', 'b', 'c', 'd', 'e']
reversed = []
for i in range(len(letters)-1,-1,-1):
    reversed.append(letters[i])
print(reversed)


"""Nested List Indexing:
Consider the nested list nested = [[1, 2, [3, 4]], [5, 6, [7, 8]]]. How would you extract the number 7 from this list using indexing"""

nested = [[1, 2, [3, 4]], [5, 6, [7, 8]]]

number = nested[1][2][0]
print(number)

"""
7. Slicing and Indexing on a String with Multiple Occurrences:
Given the string phrase = "Hello world, welcome to Python!", how would you extract thesubstring "world" 
using slicing and indexing (assuming only one occurrence)? """

phrase = "Hello world, welcome to Python!"

print(phrase[phrase.find("world"):int(phrase.find("world"))+5])



"""8. Handling IndexError in Slicing:
Given the list data = [10, 20, 30], how would you safely slice the list to get the last 5 
elements without causing an IndexError?"""

data = [10, 20, 30]

print(data[-5:])


"""
9. Multi-Dimensional Array Slicing:
For a NumPy array arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
 write a slice to extract the last column from the 2D array."""

import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

last_column = arr[:,2]

print("Array:")
print(arr)

print(last_column)



"""10. Reassigning Slices in Nested Lists:
Consider the nested list matrix = [[10, 20], [30, 40], [50, 60]]. How would you change thesecond 
element of the second inner list to 99 using indexing and slicing?"""

matrix = [[10, 20], [30, 40], [50, 60]]
print(matrix)
matrix[1][1] = 99
print(matrix)



#case part 3

""" Extract Middle Element from List: Write a Python function that takes a list of odd length and returns the middle element. 
If the list has an even length, return the two middle elements. """

def extract_middle_elements(lst):
    length = len(lst)
    
    # Check if the list is empty
    if length == 0:
        return None
    
    # Calculate the middle index
    middle_index = length // 2
    print(middle_index)
    
    # If the list has odd length, return the middle element
    if length % 2 == 1:
        return lst[middle_index]
    # If the list has even length, return the two middle elements
    else:
        return lst[middle_index - 1: middle_index + 1]

list = [1,2,3,4,5]
list1 = [1,2,3,4,5,6]

print (extract_middle_elements(list))

print (extract_middle_elements(list1))






"""Reversing a String Without Built-in Functions: Write a Python function that takesastring and 
returns it in reverse order using slicing (do not use the reversed() function)."""


def reverse_string(text):
    modified =text[-1::-1]
    return modified

print(reverse_string("my name is dawilly gene"))


"""Remove Duplicates Using Slicing: Write a Python function that takes a list and returns a new 
list with duplicates removed, keeping the original order of elements."""


def remove_duplicates(_input):
    result = []
    for i in range(len(_input)):
        if _input[i] not in _input[:i]:
            result.append(_input[i])
    return result

list2 = [1,2,1,3,4,1,3,1,11,13,4]

print(remove_duplicates(list2))



def remove_dup(_input):
    result = []

    for i in range(len(_input)):
        if _input[i] not in _input[:i]:
            result.append(_input[i])
    return result

list2 = [1,2,1,3,4,1,3,1,11,13,4]

print(remove_dup(list2))


"""Extract Every N-th Element from a List: Write a Python function that takes a list and an integer n, 
and returns a new list containing every n-th element from the original list."""


def extract_nth_elements(lst, n):
    return lst[n-1::n]




"""Check if a String is a Palindrome: Write a Python function that takes a stringandreturns 
True if the string is a palindrome (reads the same forward and backward), using slicing."""

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string reads the same forward and backward
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man a plan a canal Panama"))  # True



"""Extract a Sublist Between Two Indices: Write a Python function that takes a 
list andtwo indices (start and end) and returns a sublist containing elements fromstart
index to end index (inclusive)."""

def extract_sublist(lst, start, end):
    """
    Extracts a sublist from the given list between two indices (inclusive).

    :param lst: The original list
    :param start: The starting index
    :param end: The ending index
    :return: A sublist containing elements from start to end index (inclusive)
    """
    # Add 1 to the end index because slicing is exclusive at the end
    return lst[start:end + 1]

# Example usage
my_list = [10, 20, 30, 40, 50, 60]
start_index = 1
end_index = 4
print(extract_sublist(my_list, start_index, end_index))  # Output: [20, 30, 40, 50]



"""Create a Copy of a List Using Slicing: Write a Python function that takes a list andreturns a copy of that list using slicing"""

def copy_list(lst):
    """
    Creates and returns a copy of the given list using slicing.

    :param lst: The original list
    :return: A copy of the list
    """
    return lst[:]

# Example usage
original_list = [1, 2, 3, 4, 5]
copied_list = copy_list(original_list)

print("Original List:", original_list)  # [1, 2, 3, 4, 5]
print("Copied List:", copied_list)      # [1, 2, 3, 4, 5]

# Verify that they are separate objects
print(original_list is copied_list)    # False


"""
Find the Second Largest Element in a List: Write a Python function that takesalistof numbers 
and returns the second largest element using slicing and indexing"""

def second_largest(lst):
    """
    Returns the second largest element in a list of numbers.

    :param lst: A list of numbers
    :return: The second largest number in the list
    """
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements.")
    
    # Remove duplicates and sort the list in descending order
    unique_sorted_list = sorted(set(lst), reverse=True)
    
    # Return the second element (index 1) from the sorted list
    return unique_sorted_list[1]

# Example usage
numbers = [10, 20, 4, 45, 99, 99, 20]
print(second_largest(numbers))  # Output: 45




"""Rotate a List Left by N Elements: Write a Python function that rotates a list lst tothe left by n elements using slicing."""

def rotate_left(lst, n):
    """
    Rotates a list to the left by n elements using slicing.

    :param lst: The original list
    :param n: The number of positions to rotate
    :return: The rotated list
    """
    if not lst:
        return lst  # Handle empty list
    n = n % len(lst)  # Handle cases where n is greater than the length of the list
    return lst[n:] + lst[:n]

# Example usage
my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_left(my_list, 2)
print(rotated_list)  # Output: [3, 4, 5, 1, 2]


"""10. Replace Elements in a Range of Indices: Write a Python function that takes alist, two indices (start and end), 
and a new list of elements. 
Replace the sublist betweenthe two indices with the new list."""

def replace_sublist(lst, start, end, new_elements):
    """
    Replaces the elements in a range of indices with a new list.

    :param lst: The original list
    :param start: The starting index (inclusive)
    :param end: The ending index (inclusive)
    :param new_elements: The new list of elements to insert
    :return: The modified list
    """
    # Replace the sublist between start and end (inclusive) with new_elements
    lst[start:end + 1] = new_elements
    return lst

# Example usage
original_list = [1, 2, 3, 4, 5]
start_index = 1
end_index = 3
new_elements = [9, 10, 11]

modified_list = replace_sublist(original_list, start_index, end_index, new_elements)
print(modified_list)  # Output: [1, 9, 10, 11, 5]

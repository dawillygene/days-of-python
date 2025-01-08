text = " my name is Elia william mariki"

#print("william" not in text)  #it will print true or false according to the  context
# print(text)



set_number = {12,11,50,40}

my_list = [12,"elia","miswaki",9.84]

personal_info = {
"name" : "Elia william mariki",
"age" : "15",
"nationality" : "Tanzania"
}

my_tuple = (1, "hello", 3.14)


#slicing 

word ="Extraordinary is safe"

#[start:end:step]
print(word[0:5]) #Extra
print(word[5:])
print(word[5:13])
print(word[0:13:2])

print(word[::-1]) #reverse the order yranidroartxE

print(word.isalpha()) #check if all characters Alphabetic Characters: Only letters (a-z, A-Z) are considered alphabetic.
print(word.isalnum())
print(word.isdigit()) # Checks if all characters are digits.
print(word.isspace()) # Checks if all characters are whitespace.


print(word.lower())
print(word.upper())
print(word.capitalize())
print(word.title())
print(word.strip())  #removes white space before and after
print(word.lstrip())
print(word.rstrip())
print(word.replace("safe","danger"))
print(word.find("safe")) #returning the -1 if the substring not found if it found return its index
print(word.index("safe"))
print(word.count("a")) #count the number of substrings

word1 ="Extraordinary is safe"

print(word1.split(","))
print(word1.split(maxsplit=1))


words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # Output: "Hello World Python"

words = ["apple", "banana", "cherry"]
result = ", ".join(words)
print(result)  # Output: "apple, banana, cherry"

fruits = ("apple", "banana", "cherry")
result = " and ".join(fruits)
print(result)  # Output: "apple and banana and cherry"


print(word.startswith("Extra"))
print(word.endswith("safe"))
print(word.swapcase())

number = "12";
#string.zfill(width)
print(number.zfill(5))
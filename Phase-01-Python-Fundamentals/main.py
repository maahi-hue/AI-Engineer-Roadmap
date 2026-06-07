from unittest import result

print("Hello World")

# variables and data types
character_name = "Tom"  #string
character_age = 20      #number
is_male = True          #boolean (True/False)
# print("There once was a man named " + character_name + "," )
# print("he was " + str(character_age) + " years old")
# print("He really liked the name " + character_name + ",")
# print("but didn't like being " + str(character_age) + " years old")

# working with strings
phrase = "Giraffe Academy"
# print(phrase.upper().isupper())   #(uppper()/lower() -> uppercase/lowercase
                                  #(isupper()/islower() -> to check case
# print(len(phrase))                #length
# print(phrase[0])                  #to get strings by index
# print(phrase.index("G"))          #to get index by character
# print(phrase.replace("G", "O"))

# working with numbers
# print(3 * (4 + 5))             #parenthesis to specify order of operations
# print(10 % 3)                  #mod to find remainder
my_number = -10
# print(abs(my_number))          #absolute value
# print(pow(3, 2))               #3^2
# print(max(4, 6))               #max/min
# print(round(3.2))              #round number

from math import *             #math module to access more math functions
# print(floor(3.2))              #chop off the decimal point and get the lowest number
# print(ceil(3.2))
# print(sqrt(36))                #square root of a number

# getting input from user
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# lists
friends = ["kevin", "karen", "jim", "Oscar", "Toby"]
friends[1] = "mike"
# print(friends[1:])
# print(friends[1:3])

# list functions
lucky_numbers = [4, 42, 8, 15, 16, 23 ]
friends = ["kevin", "karen", "jim", "Oscar", "Toby", "jim", "jim"]
friends2 = friends.copy()                    #copy a list
# print(friends2)
friends.extend(lucky_numbers)                #add lists
friends.append("creed")                      #add additional item in the end
friends.insert(1, "kelly")      #add item in a specific index
friends.remove("jim")                        #remove item
friends.pop()                                #remove last element in the list
friends.clear()                              #remove whole list
lucky_numbers.sort()
lucky_numbers.reverse()
# print(lucky_numbers)
# print(friends)
# print(friends.count("jim"))

# tuples
coordinates = [(4, 5), (6, 7), (80, 34)]
# coordinates[1] = 10                          #this gives error because tuples can not be changed or modified like lists
# print(coordinates[0])

# functions
# def say_hi(name, age, gender):
    # print("Hello " + name + ", you are " + str(age) + " years old " + gender )

# say_hi("mike", 20, "Male")

# return statement
# def cube(num):
#     return num*num*num
#
# result = cube(3)
# print(result)

# if statement
is_male = False
is_tall = True

# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("you are not a male and not tall")

# if statements & comparisons
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(3,4,5))

# dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# print(monthConversions["Jan"])
# print(monthConversions.get("Feb"))

# while loop
i = 1
while i <= 10:
    # print(i)
    i += 1

# print("Done with loop")

# for loop
friends = ["kevin", "karen", "jim", "Oscar", "Toby"]
# for friend in  friends:
    # print(friend)

# for index in range(len(friends)):
#     print(friends[index])
#
# for index in range(3, 10):
#     print(index)
#
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("not first iteration")


# exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

# print(raise_to_power(3,4))

# 2D lists & nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(number_grid[0][0])

# for row in number_grid:
#     for col in row:
        # print(col)


# try except
# try:
    # number = int(input("Enter a number: "))
    # print(number)
# except ZeroDivisionError as err:
    # print(err)
# except ValueError:
    # print("Invalid input")


# reading files
file = open("structure.txt", "r")            #there are multiple mode like- r->read, w->write, a->append, r+->read+write
# for lines in file.readlines():
    # print(lines)                             #reads each line of the file

# print(file.readable())                     #checks if the file is readable or not return True/False according to the mode
# print(file.read())                         #reads whole file
# print(file.readline())                     #reads first line
# print(file.readlines())                    #reads all lines of the file as an array
# print(file.readlines()[1])
file.close()


# writing files
file = open("structure.txt", "a")
# file.write("\nrdfghg")
file.close()


# modules and pip
#list of python modules (google)

# classes & objects
from student import student
student1 = student("Jim", "Business", 3.1, False)
student2 = student("Pam", "Art", 2.5, True)

# print(student2.gpa)
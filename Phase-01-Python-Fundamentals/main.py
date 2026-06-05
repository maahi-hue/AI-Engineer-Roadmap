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
def say_hi(name, age, gender):
    print("Hello " + name + ", you are " + str(age) + " years old " + gender )

say_hi("mike", 20, "Male")
say_hi("jim", 20, "Female")
say_hi("karen", 20, "Male")
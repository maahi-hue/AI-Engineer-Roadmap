print("Hello World")

# variables and data types
character_name = "Tom"  #string
character_age = 20      #number
is_male = True          #boolean (True/False)
print("There once was a man named " + character_name + "," )
print("he was " + str(character_age) + " years old")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + str(character_age) + " years old")

# working with strings
phrase = "Giraffe Academy"
print(phrase.upper().isupper())   #(uppper()/lower() -> uppercase/lowercase
                                  #(isupper()/islower() -> to check case
print(len(phrase))                #length
print(phrase[0])                  #to get strings by index
print(phrase.index("G"))          #to get index by character
print(phrase.replace("G", "O"))

# working with numbers
print(3 * (4 + 5))             #parenthesis to specify order of operations
print(10 % 3)                  #mod to find remainder
my_number = -10
print(abs(my_number))          #absolute value
print(pow(3, 2))               #3^2
print(max(4, 6))               #max/min
print(round(3.2))              #round number

from math import *             #math module to access more math functions
print(floor(3.2))              #chop off the decimal point and get the lowest number
print(ceil(3.2))
print(sqrt(36))                #square root of a number


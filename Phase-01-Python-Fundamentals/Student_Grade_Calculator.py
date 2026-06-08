name= input("Enter your name: ")
sub = int(input("Enter number of subjects: "))

max_marks = float(input("Enter maximum marks of each subject: "))

Total = sub * max_marks
obt = 0

for i in range(sub):
    marks = float(input(f"Enter marks of subject {i+1}: "))
    obt = obt + marks

percent = (obt * 100) / Total

if(percent >= 80):
    grade = "A+"
elif(percent >= 70):
    grade = "A"
elif(percent >= 60):
    grade = "B"
elif(percent >= 50):
    grade = "C"
elif(percent >= 40):
    grade = "D"
elif(percent >= 33):
    grade = "F"


print(" ")
print("---------RESULT---------")
print(" ")
print(f"Student Name: {name}")
print(f"Total Marks: {Total}")
print(f"Obtained Marks: {obt}")
print(f"Percentage: {percent:.2f}%")
print(f"Grade: {grade}")

# print(f"Marks: {obt}/{Total}")
#
# print(f"Marks: {obt}/{Total} with percentage: {percent}%")
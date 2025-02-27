# Variables in Python
student_name = "John" # string
student_second_name = "Doe" # string
student_age = 20 # integer
student_height = 1.80 # float
student_admitted = True # boolean

# Operators in Python
# 1. Arithmetic operators
num1 = 10
num2 = 20
addition = num1 + num2
# print(addition)
substraction = num1 - num2
# print(substraction)

#2. Comparison operators
print(num1 == num2) # False
print(num1 != num2) # True
print(num1 > num2) #  False
print(num1 < num2) # True

#3. Logical operators
# and, or, not
# print(num1 < num2 and num1 > num2) # False
# print(num1 < num2 or num1 < num2) # True
# print(not num1 < num2) # False

#4. Assignment operators
# =, +=, -=, *=, /=
# num1 +=5
# print(num1) # 15
# num1 -=5
# print(num1) # 10
# num1 *=5
# print(num1) # 50

#5. Identity operators
# is, is not
# print(num1 is not num2) # True
# print(num1 is num2) # False

#6. Membership operators
# if, elif, else

if student_age >= 18:
    print('You are an adult')

enter_name = input('Enter your name: ')
enter_age = int(input('Enter your age: '))
if enter_age >= 18:
    print('You are an adult')

enter_speed = input('Enter your speed: ')
enter_speed = int(enter_speed)

# print the entered sppeed data type
print(type(enter_speed))







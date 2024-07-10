import math


#1

#зроблене


# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     print(f"Hello, {name}! Your age is {age}")
# except Exception:
#     print("Invalid value")
# if age < 0:
#     print("Invalid value")
# elif age > 130:
#     print("Invalid value")



#2

#зроблено


#2.1

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# def fullname(name, age):
#       print(f"Hello, {name}! Your age is {age}")


    
# if age < 0:
#     print("Invalid value")
# elif age > 130:
#     print("Invalid value")

# print(fullname(name,age))



#2.2

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# def fullname(name, age):
#     try:
#       print(f"Hello, {name}! Your age is {age}")
#     except Exception:
#        print("Invalid value")
#     if age < 0:
#       print("Invalid value")
#     elif age > 130:
#        print("Invalid value")

# print(fullname(name,age))


#3


#зроблене

# try:
#  num_1 = int(input("Введіть число, більше за нуль: "))
#  num_2 = int(input("Введіть число, більше за нуль: "))
#  num_3 = int(input("Введіть число, більше за нуль: "))
#  num_4 = int(input("Введіть число, більше за нуль: "))
#  num_5 = int(input("Введіть число, більше за нуль: "))
#  list = [num_1,num_2,num_3,num_4,num_5]
# except ValueError:
#  print("Number is not positive")
# for i in list:
#    if i <=0:
#      print("Number is not positive")
#    else:
#      print(sum(list))

#4


#зроблене


#4.1
# num_1 = int(input("Введіть число, більше за нуль: "))
# num_2 = int(input("Введіть число, більше за нуль: "))
# num_3 = int(input("Введіть число, більше за нуль: "))
# num_4 = int(input("Введіть число, більше за нуль: "))
# num_5 = int(input("Введіть число, більше за нуль: "))
# list = [num_1,num_2,num_3,num_4,num_5]

# def printSum(list):
#       print(sum(list))


# for i in list:
#    if i <=0:
#      print("Number is not positive")
#    else:
#      print(sum(list))


# print(printSum(list))
    


#4.2

# num_1 = int(input("Введіть число, більше за нуль: "))
# num_2 = int(input("Введіть число, більше за нуль: "))
# num_3 = int(input("Введіть число, більше за нуль: "))
# num_4 = int(input("Введіть число, більше за нуль: "))
# num_5 = int(input("Введіть число, більше за нуль: "))
# list = [num_1,num_2,num_3,num_4,num_5]

# def printSum(list):
#    for i in list:
#     if i <=0:
#       print("Number is not positive")
#     else:
#       print(sum(list))

# print(printSum(list))
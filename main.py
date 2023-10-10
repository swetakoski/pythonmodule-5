# Module 5
#Question 1: lls all the dice once and prints out the sum of the numbers.
# Use a for loopWrite a program that asks the user how many dice to roll.
# # The program ro

# import random
# dice = int(input("How many dice do you want to roll? "))
#
#
# def roll_dice(num_dice):
#     rolls = 0
#     for i in range(1, num_dice + 1):
#         print(f"Roll #{i} = {(roll := random.randint(1, 6))}")
#         rolls += roll
#     return rolls
#
#
# result = roll_dice(dice)
# print(f"The total for {dice} rolls is {result}.")
#
# name=[]
# name=input("Enter you name: ")
# index=0
# while name!="" and index<len(name):
#     print(name[index])
#     index =index +1

sentence=input("Type a sentence: ")
sentence=" " + sentence
index_num=1
while index_num<len(sentence):
        print(sentence[index_num])
        index_num =index_num +1




#Question 2: Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

# numbers=[]
# while numbers !="":
#     number=input("Enter your numbers:  or press Enter to quit: ")
#     numbers.append(number)
#     numbers.sort(reverse=True)
#     if number =="":
#         break
# print(numbers[:5])


# Question 3: Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

# number = int(input("Enter a number: "))
#
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(f"{number} is not a prime number")
#             break
#     else:
#         print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# Question no 4: Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
# and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.


# city_list = []
# for i in range(5):
#     city=input("Enter your city :  ")
#     city_list.append(city)
# print("Cities entered: ")
# for city in city_list:
#     print (city)


# Angelina Del Vicario
# CMP 131
# week 5
# Lab 4
#Temperature category
# 9/18/26

print ("_____WELCOME_____")
#welcome header
temp = float(input("Please enter the temperature outside: "))
#to input temp and make it useable with a decimal
if (temp >= 80):
    print("The Weather is Hot")
elif (temp >= 79):
    print("The Weather is Warm")
elif (temp >50):
    print("The Weather is Warm")
elif(temp <= 49.9):
    print("The Weather is Cold")
else:
    print("The Weather is Very Hot")
#different temp conditions


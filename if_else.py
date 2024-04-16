# if else
"""

num = int(input("Enter any number:"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

"""

# nested if else
"""

height = int(input("Enter your height in cm:"))
if (height>=120):
    print("you can ride roller coaster\n")
    age = int(input("Enter your age:"))
    if(age<12):
        print("You have to pay $7")
    elif(age>=12 and age <=18):
        print("you have to pay $12")
    else:
        print("you have to pay $17")
else:
    print("sorry your height is short,please grow your height")

"""

# leap year

year = int(input("Enter a year which you want to check:"))
if((year % 4 == 0 )and ((year % 100!=0) or (year % 400 == 0))):
    print ("year is leap year")
else:
    print ("year is not a leap year")

 
from random import randint
computer = randint(1,100)
while (True):
    user = int(input("Guess the number:"))
    if(user > computer):
        print("Sorry, the number is less")
        
    elif(user < computer):
        print("Sorry, the number is high")
        
    else:
        print("Yes, you guess it right!!!\nYou won")
        break

        


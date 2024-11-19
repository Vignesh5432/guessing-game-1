import random
print("Guessing Game Between The user and the machine")
user=input("Enter your mode of play(user,machine,exit):")
if user=="user":
    print("follow the Instructions given below")
    print("First of all,You need to guess the number that have been chosen by the machine")
    print("After each guess, the machine will tell whether it's high or low or correct")
    low=int(input("set the lower range for the guess:"))
    high=int(input("set the upper range for the guess:"))
    num_of_guess = random.randint(low,high)
    while True:
        guess=int(input(f"guess a  number between {low} and {high}:"))
        if(guess < num_of_guess):
            print("Too low")
            low = guess+1
        elif(guess > num_of_guess):
            print("Too high")
            high=guess-1
        else:
            print(f"Correct")
            break
elif user=="machine":
    print("Follow the Instruction given below:")
    print(" Now think a number within the range you set")
    print("The machine will try to guess the number")
    low=int(input("Enter alower range:"))
    high=int(input("Enter a upper range:"))
    attemp=0
    while True:
        Guess=(low+high)//2
        print(f"my Guess is:{Guess}")
        end=input("enter 'higher' or 'lower' or 'correct':")
        if(end=="higher"):
            low=Guess+1
        elif(end=="lower"):
            high=Guess-1
        elif(end=="correct"):
            print("won","\t the game is over")
            break
else:
    print("Thank you")

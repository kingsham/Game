#!usr/bin/env python3

import random

number = random.randint(1,10) # Generates numbers 1 through 10 randomly
win=False
tries=0
username=input("What is you username ?") # user inputs their name

print("Hello",username + ",",) 

question=input("Would you like to play a game?[Y/N]") # The program asks the user if he/she wants to play or not
if question.lower() == "n":
    print("oh..okay")
    exit()
if question.lower() == "y":
    print("I'm thinking of a number between 1 & 10") 
while not win:
    guess = int(input("Have a guess: ")) # Allows user to enter the guess number
    tries=tries+1
    if guess == number: # if the the number the user entered is correct you have won
        win = True
    elif guess < number: # if the number the user entered is lower than the guess number then the program will say the print statement
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower")
if guess == number:
    print("You got it ! the number is ", number, \
           "and it only", tries,"took tries !")


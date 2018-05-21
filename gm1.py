#!usr/bin/env python3

import random

number = random.randint(1,10)
win=False
tries=0
username=input("What is you username ?")

print("Hello",username + ",",)

question=input("Would you like to play a game?[Y/N]")
if question.lower() == "n":
    print("oh..okay")
    exit()
if question.lower() == "y":
    print("I'm thinking of a number between 1 & 10")
while not win:
    guess = int(input("Have a guess: "))
    tries=tries+1
    if guess == number:
        win = True
    elif guess < number:
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower")
if guess == number:
    print("You got it ! the number is ", number, \
           "and it only", tries,"took tries !")


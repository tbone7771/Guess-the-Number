import random
import time
p = 100 ##starting points, optional input
n = random.randint(1, p) ## picks the random number
m = 1 ##starting multiplier
d = .1 ##difficulty


print("Welcome to Guess the Number!")
time.sleep(2)
print("You will get points based on how many guesses it takes you to guess the number")
time.sleep(3.75)
print("I am thinking of a number between 1 and " + str(p))
print()
time.sleep(2.75)
print("What is your guess for " + str(p) + " points?")
g = int(input()) ## first guess
print()


while 1 == 1:
    if n == g:
        print("Congrats! You guessed the number for " + str(p) + " points!")
        break
    elif n < g:
        print("The Number is lower than " + str(g))
        p -= int(m * random.randint(5,15))
        m += d
        if p < 0:
            print("Sorry, you lose")
            break
        print("Guess again for " + str(p) + " points!")
        g = int(input())
        print()
    elif n > g:
        print("The Number is higher than " + str(g))
        p -= int(m * random.randint(5,15))
        m += d
        if p < 0:
            print("Sorry, you lose")
            break
        print("Guess again for " + str(p) + " points!")
        g = int(input())
        print()
    elif p < 0:
        print("Sorry, you lose")
        break
print("The number was: " + str(n))

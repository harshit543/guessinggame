from random import randint
import sys
#generate a number 1 to 10
answer=randint(1,10)
#input from user?
#check that input is a number 1 to 10
while True:
    try:
        guess = int(input('guess a number 1 to 10:\n'))
        if 0<guess<11:
            if guess==answer:
                print('you are a genius man')
                break
        else:
            print('hey moron, I said 1 to 10')
    except ValueError:
        print('enter a number')
#check if number is the right guess. Othervise
#ask again.

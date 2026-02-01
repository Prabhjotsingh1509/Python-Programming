'''
Docstring for Python-Practice.Chapter-9(small-project).snake,water,
snake = 1
water = -1
gun = 0
'''

import random

computer=random.choice([-1,0,1])
you= input("Enter the choice:")

yourdict={
    "s":1,
    "w":-1,
    "g":0
}
user=yourdict[you]

reversedict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}

print(f"You Choose :{reversedict[user]}\nComputer choose:{reversedict[computer]}")

if(computer == user):
    print("Game Draw")
else:
    '''
    if(computer==1 and user==-1):
        print("You lose!")
    elif(computer==1 and user==0):
        print("You win!")
    elif(computer==-1 and user==1):
        print("You win!")
    elif(computer==-1 and user==0):
        print("You lose!")
    elif(computer==0 and user==1):
        print("You lose!")
    elif(computer==0 and user==-1):
        print("You win!")
    else:
        print("something went wrong")
    '''
    if((user - computer)== -2 or (user - computer)== 1):
        print("You lose")
    else:
        print("You win")
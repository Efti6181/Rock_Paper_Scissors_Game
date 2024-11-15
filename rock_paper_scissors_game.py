
'''
Rock=1
paper=-1
scissors=0
'''
import random

computer = random.choice([-1,0,1])
yourch= input("Enter your choice among these: rock , paper, scissors:    ")
Y_Dict = {"rock":1, "paper":-1,"scissors":0}
r_dict = {1:"rock",-1:"paper", 0:"scissors"}
cc=print(f"computer choice is {r_dict[computer]}")
you=Y_Dict[yourch]
if(computer==you):
    print("It's a draw")
else:
    if(computer==1 and you==-1):
        print("You win")
    elif(computer==-1 and you==0):
        print("You win")
    elif(computer==0 and you==1):
        print("You win")
    elif(computer==-1 and you==1):
        print("You loss")
    elif(computer==0 and you==-1):
        print("You loss")
    elif(computer==1 and you==0):
        print("You loss")
    else:
        ("Somethin went wrong")

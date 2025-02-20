print("-----------welcome game zone -------------")
print("how to play game ?")
print("s is snake w is water g is gun")
print("example:1")
print("user choice is 1 and computer choice is 0 user is winer because user number is big")
print("user choice is  s,w,g")

import random
user = input("enter your choice: ")


dics = {
    "s": 1, "w" : -1, "g" : 0
}

you  = dics[user]
com =  random.choice([1,0,-1])

if(com == you):
    print("with draw")

else:
     if(com == 0 and you == 1):
        print("user is winer")
     elif(com == 1 and you == 0):
        print("user is loser")
     if(com == -1 and you == 0):
        print("loser is winer")
     elif(com == 1 and you == 1):
        print("with draw")
     if(com == 1 and you == 1):
        print("with draw")
     elif(com == -1 and you == 1):
        print("user is winer")
     if(com == 1 and you == -1):
        print("user is loser")
     elif(com == 0 and you == -1):
        print("user is winerr")





print(f"user choice is {you}\ncomputer choice is {com}")



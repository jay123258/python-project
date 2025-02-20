import random


a = random.randint(1,100)


while True:
    user = int(input("enter your number: "))

    if user <a:
        print("enter your higher number: ")

    elif user > a:
        print("enter your lawer number: ")

    else:
        print(f"congratulation your choice is  {a}")
        break
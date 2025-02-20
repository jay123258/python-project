import time

user = int(input("enter your second: "))


for i in range(user,0,-1):
    second = i % 60
    print(f"00:00:{second:02}")
    time.sleep(1)

print("TiME'S UP")
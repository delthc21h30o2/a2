import random


user_score = 0
computer_score = 0

while user_score <4 and computer_score <4:
    x = random.randint(1, 3)
    if x==1:
        computer="sang"

    elif x==2:
        computer="kaghaz"

    elif x==3:
        computer="gheychi"

    user= input("guess: ")

    print(computer)
    print(user)

    if computer =="sang" and user == "sang":
        print("mosavi")

    elif computer == "sang" and user== "kaghaz":
        print("user win")
        user_score=user_score+1

    elif computer == "sang" and user== "gheychi":
        print("computer win")
        computer_score=computer_score+1

    elif computer == "kaghaz" and user =="kaghaz":
        print("mosavi")

    elif computer == "kaghaz" and user == "sang":
        print("computer win")
        computer_score=computer_score+1

    elif computer == "kaghaz" and user == "gheychi":
        print("user win")
        user_score=user_score+1

    elif computer == "gheychi" and user == "gheychi":
        print("mosavi")

    elif computer == "gheychi" and user == "sang":
        print("user win")
        user_score=user_score+1

    elif computer == "gheychi" and user == "kaghaz":
        print("computer win")
        computer_score=computer_score+1

print("you", user_score)
print("computer", computer_score)
if user_score>computer_score:
    print("you win")
elif user_score<computer_score:
    print("computer win")
print("the end")
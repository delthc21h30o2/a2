import random

userG=0
computerN= random.randint(10,30)
for i in range(10):
    userN= int(input("guess a number: ")) 
    
    if computerN == userN:
        print("you win") 
        print("❤️❤️❤️❤️❤️")
        userG=userG+1
        break

    elif computerN > userN:
        print("bishtare")
        userG=userG+1

    else:
        print("kamtare")
        userG=userG+1

print(userG)

    
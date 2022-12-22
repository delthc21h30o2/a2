from asyncio import tasks
import random
print("welcome to tass")
while True:
    tass=random.randint (1,6)
    print(tass)
    if tass !=6:
        c=input(("enter exit to end: "))
        if c == "exit":
            break
    elif tass== 6:
        print("throw again")

print("end")
avg=0
c=0
print("enter y in exit to exit")
while True:
    usc=float(input("enter score: "))
    exi= input("exit? ")
    avg=avg+usc
    c=c+1
    if exi=="y":
        break

ans= avg/c
print(ans)

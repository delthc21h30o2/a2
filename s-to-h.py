user= int(input("enter sec: "))

h= user//3600
b=user%3600
m=b//60
s=b%60


print(h,":",m,":",s)
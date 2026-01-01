a=int(input("enter a number: "))
b=int(input("enter b number: "))
x,y=a,b
while y!=0:
    x,y=y,x%y
gcd=x
lcm=(a*b)//gcd
print("lcm: ",lcm)
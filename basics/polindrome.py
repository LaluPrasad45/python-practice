j=int(input("enter a number: "))
rev_j=int(str(j)[::-1])
print("the reverse of",j,"is: ",rev_j)
if j==rev_j:
    print(f"{j} is a polidrome")
else:
    print(f"{j} is not a polindrome")
    
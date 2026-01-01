l=str(input("enter a string: "))
j=0
v=['a','e','i','o','u']
for i in l:
    if i in v:
        j+=1
print(j)
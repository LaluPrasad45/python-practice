l=[7,0,45,18,2,7,45]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i])
            break


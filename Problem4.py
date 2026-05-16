lis = list(map(int,input().split()))
target = int(input())
new_lis = []
for i in lis:

    for j in lis:

        if i + j == target:

            new_lis.append(i)
            new_lis.append(j)
            

print(new_lis)
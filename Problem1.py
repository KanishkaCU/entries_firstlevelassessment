#second largest in an array
num = list(map(int,input().split()))

largest = 0

for i in num:
    if i>largest:
        largest = i

num.remove(largest)

second_largest = 0

for j in num:
    if j > second_largest:
        second_largest = j

print(second_largest)
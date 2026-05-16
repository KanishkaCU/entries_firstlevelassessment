s = input()
original = s

for i in s:
    if i == " ":
        s.remove(i)
        
print(s)

s1 = s[::-1]

print(s1)

if original == s1:
    print("True")
else:
    print("False")




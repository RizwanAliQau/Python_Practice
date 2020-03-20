a = [1, 2 ,3 ,4 ,5,5,4,3 ,3]
b = []
for num in a:
    if num not in b:
        b.append(num)
print(b)

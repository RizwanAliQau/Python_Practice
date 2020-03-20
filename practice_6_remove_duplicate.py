a = [2, 2 , 3 , 4, 4, 5,5, 13, 20 ,2]
b = a.copy()
len_a = len(a)
r= 0
c= 0
for i in range(len_a-1):
    r = r+i+1
    for k in range(r,len_a):
        print(k)
        if a[i] == a[k]:

            b[k] = 0
            c = c + 1
    r = 0

b.remove(0)
print(b)





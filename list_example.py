name = ['riz', 'rizw', 'rizwan']
len_list= len(name)
a = [0, 0, 0]
for i in range(len_list):
    a[i] = len(name[i])
b = max(a)
for j in range(len_list):
    if b == a[j]:
        c = j
print('the largest name is: ')
print(name[c])



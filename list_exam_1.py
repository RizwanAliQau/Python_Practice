a = [1, 2, 3]
print(a)

a.append('d')
print(a)

a.extend([4, 5, 6])
print(a)

print(a.count(1))

print(a.index(3))

a.remove('d')
print(a)

a.sort()
print(a)

a.reverse()
print(a)

# operators also used to extend the list

a += [7, 8]
print(a)

a = a * 2
print(a)

# slicing

b = a[3:6:1]
print(b)

# list comprehension

new_list = [i for i in range(10) if i % 2 == 0] # ir replaces the for loop with if condition enclosed in it
print(new_list)

# example list comprehension, filtering list
n_l = [3, 4, 5, 6]
n_l_filt = [i * 3 for i in n_l if i % 3 == 0 ]
print(n_l_filt)

c_list = n_l.copy()
print(c_list)

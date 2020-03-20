numbers = [5, 2, 5, 2, 2]
for pattern in numbers:
    print('*' * pattern)


#### By nested loop

for pat in numbers:
    count = ''
    for i in range(pat):
        count += "*"
    print(count)


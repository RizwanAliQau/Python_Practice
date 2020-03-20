import random

for i in range(3):
    print(random.random()) # 0 to 1

for i in range(3):
    print(random.randint(10,20)) # between particular range

# randomly pick a member
members = ['rizwan', 'ali', 'shah']
leader = random.choice(members)
print(leader)


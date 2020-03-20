

message = input("--->")
words = message.split()
print(words)

emoji = {":)": '😊', ":(": '😒', ";)":'😉' }

mess=''

for i in words:
    temp = emoji.get(i)
    if temp!=None:
        mess += str(temp)

    else:
        mess+=i
    mess+= ' '

print(mess)


#### another way to do that program

mess_1 =''
for word in words:
    mess_1 += emoji.get(word, word) + ' '

print(mess_1)


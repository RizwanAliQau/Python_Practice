try:
    num = int(input("enter a number"))
    sq_num = num*num
    print(sq_num)
    num1= int(input("enter second number of division"))
    b = num / num1
except ValueError:
    print('invalid number')
except ZeroDivisionError:
    print("num2 can't be zero")
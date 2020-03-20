dict = {"0": "Zero","1": "One", "2": "Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Sevem",
        "8":"Eight","9":"Nine"}


phone= input("Phone:")
p = ""
for cod in phone:
    p+=  dict.get(cod)
    p+= " "
print(p)
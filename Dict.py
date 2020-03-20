
# Each key should be unique
customer = {"name": "rizwan" , "age": 28, "is_verf": True}
print(customer["name"])
print(customer.get("birthday"))
print(customer.get("birthday", "jan 8,1992"))

# add new pair value key by using the assignment
customer["birth"]="nov 2000"
print(customer["birth"])

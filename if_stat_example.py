# Price of house is 1M if the buyer have good credit he pays 10% and else 20% down payment
Price = 1000000;
good_credit = True

if good_credit:
    print('The down payment is:')
    pays = 0.1 * Price
    print(pays)
else:
    print('The down payment is:')
    pays = 0.2 * Price
    print(pays)


print('the other way to print')
print(f"Down Payment: {pays}")


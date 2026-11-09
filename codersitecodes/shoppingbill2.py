import sys

def calculate_total(price,quantity):
    return price * quantity

data = sys.stdin.read().split()

price = float(data[0])
quantity = int(data[1])

result = calculate_total(price, quantity)

if result == int(result):
    print(int(result))
else:
    print(result)
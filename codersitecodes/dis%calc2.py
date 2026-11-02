import sys

discount = lambda price, percentt: price * percentt / 100

data = sys.stdin.read().split()
price, percentt = float(data[0]), float(data[1])
print(discount(price, percentt))
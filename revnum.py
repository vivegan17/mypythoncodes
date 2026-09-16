def revnum(num):
 rev = 0
 while num > 0:
  rev = (rev * 10) + num % 10
  num=num//10
 return rev
num = int(input("enter a num to reverse :"))
numrev = revnum(num)
print(numrev)
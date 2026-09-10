def eveodd (x) :
  if(x%2==0):
    print("even")
  elif(x==1):
    print("neither odd or even")
  else:
    print("odd")
x=int(input("enter number :"))
eveodd(x)
import numpy as np
arr=np.array([10,20,30,47,74])
arr[arr>40]+=10
print(arr)
print(arr.T)
bonus = np.array([5])
print(arr+bonus)
a = np.random.randint(1, 77, size=5)
print(a)
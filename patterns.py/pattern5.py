class Solution:
    def pattern5(self, n):
        k = n
        for i in range(1,n+1):
            print("*" * k)
            k-=1
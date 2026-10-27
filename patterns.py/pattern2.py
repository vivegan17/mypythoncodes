class Solution:
    def pattern2(self, n):
        k=1
        for i in range(0,n):
            print("*" * k)
            k+=1
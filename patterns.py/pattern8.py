class Solution:
    def pattern8(self, n):
        for i in range(n):
            stars = "*" * ((2*n) - 1)
            spaces = " " * ((i+1) - 1)
            n-=1
            print(spaces+stars)
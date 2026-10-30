class Solution:
  def pattern9(self, n):
    for i in range(n):
      spaces = ' ' * (n - i - 1)
      stars = '*' * (2 * i + 1)
      print(spaces + stars)

    
    for i in range(n - 1, 0, -1):
      spaces = ' ' * (n - i )
      stars = '*' * (2 * i - 1)
      print(spaces + stars)

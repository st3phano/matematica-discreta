'''
P(1) = 1
P(n) = n ** 2 * P(n - 1) + n - 1, para n >= 2
'''

def P(n):
   if (n == 1):
      return 1
   return n ** 2 * P(n - 1) + n - 1

for n in range(1, 11):
   print(f"P({n}) = {P(n)}")

'''
B(1) = 1
B(n) = B(n - 1) + n ** 2, para n >= 2
'''

def B(n):
   if (n == 1):
      return 1
   return B(n - 1) + n ** 2

for n in range(1, 11):
   print(f"B({n}) = {B(n)}")

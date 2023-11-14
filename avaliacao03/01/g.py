'''
T(1) = 1
T(2) = 2
T(3) = 3
T(n) = T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3), para n > 3
'''

def T(n):
   if (n == 1):
      return 1
   if (n == 2):
      return 2
   if (n == 3):
      return 3
   return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)

for n in range(1, 11):
   print(f"T({n}) = {T(n)}")

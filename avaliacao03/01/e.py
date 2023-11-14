'''
D(1) = 3
D(2) = 5
D(n) = (n - 1) * D(n - 1) + (n - 2) * D(n - 2), para n > 2
'''

def D(n):
   if (n == 1):
      return 3
   if (n == 2):
      return 5
   return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

for n in range(1, 11):
   print(f"D({n}) = {D(n)}")

'''
W(1) = 2
W(2) = 5
W(n) = W(n - 1) * W(n - 2), para n > 2
'''

def W(n):
   if (n == 1):
      return 2
   if (n == 2):
      return 5
   return W(n - 1) * W(n - 2)

for n in range(1, 11):
   print(f"W({n}) = {W(n)}")

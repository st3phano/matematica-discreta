def S(n):
   if (n == 1):
      return "p"
   return S(n - 1) + " + q" + " * -1"

for n in range(1, 7):
   print(f"S({n}) = {S(n)}")

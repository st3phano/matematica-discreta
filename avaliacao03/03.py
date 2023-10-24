def T(x):
   if (x < 2):
      return False
   if (x == 2):
      return True
   return T(x - 3) or T(x / 2)

for x in range(2, 20):
   print(f"T({x}) = {T(x)}")

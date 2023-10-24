def M(x):
   if (x < 2):
      return False
   if (x == 2 or x == 3):
      return True
   return M(x / 2) or M(x / 3)

numeros = [2, 3, 6, 9, 16, 21, 26, 54, 72, 218]
for x in numeros:
   print(f"M({x}) = {M(x)}")

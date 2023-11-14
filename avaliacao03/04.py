'''
Uma coleção M de números é definida recursivamente por:
2 ∈ M e 3 ∈ M
Se X ∈ M e Y ∈ M, então X * Y ∈ M
Quais dos seguintes números pertencem a M? 6, 9, 16, 21, 26, 54, 72, 218
'''

def M(x):
   if (x < 2):
      return False
   if (x == 2 or x == 3):
      return True
   if ((x % 2 == 0) or (x % 3 == 0)):
      return M(x / 2) or M(x / 3)
   return False

numeros = [6, 9, 16, 21, 26, 54, 72, 218]
for x in numeros:
   print(f"M({x}) = {M(x)}")

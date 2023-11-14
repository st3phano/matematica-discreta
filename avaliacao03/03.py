'''
Uma coleção T de números é definida recursivamente por:
2 ∈ T
Se X ∈ T, então X + 3 ∈ T e 2 * X ∈ T
Quais dos seguintes números pertencem a T? 6, 7, 19, 12
'''

def T(x):
   if (x < 2):
      return False
   if (x == 2):
      return True
   if ((x - 3 > 2) or (x % 2 == 0)):
      return T(x - 3) or T(x / 2)
   return False

numeros = [6, 7, 19, 12]
for x in numeros:
   print(f"T({x}) = {T(x)}")

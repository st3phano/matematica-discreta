'''
Uma coleção W de cadeias de símbolos é definida recursivamente por:
a ∈ W, b ∈ W e c ∈ W
Se X ∈ W, então a(X)c ∈ W
Quais das seguintes cadeias pertencem a S? a(b)c, a(a(b)c)c, a(abc)c, a(a(a(a)c)c)c, a(aacc)c
'''

def W(x):
   if (x == "a" or x == "b" or x == "c"):
      return True
   if ((x[ : 2] == "a(") and (x[-2 : ] == ")c")):
      return W(x[2 : -2])
   return False

cadeias = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]
for x in cadeias:
   print(f"W({x}) = {W(x)}")

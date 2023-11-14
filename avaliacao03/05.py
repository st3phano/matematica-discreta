'''
Uma coleção S de cadeias de caracteres é definida recursivamente por:
a ∈ S e b ∈ S
Se X ∈ S, então Xb ∈ S
Quais das seguintes cadeias pertencem a S? a, ab, aba, aaab, bbbbb
'''

def S(x):
   if (x == "a" or x == "b"):
      return True
   if ((x[ : 2] == "ab") or (x[ : 2] == "bb")):
      return S(x[1 : ])
   return False

cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]
for x in cadeias:
   print(f"S({x}) = {S(x)}")

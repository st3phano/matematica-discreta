def S(x):
   if (x == "a" or x == "b"):
      return True
   if (x[ : 2] == "ab" or x[ : 2] == "bb"):
      return S(x[1 : ])
   return False

cadeias = ["a", "b", "ab", "aba", "aaab", "bbbbb"]
for x in cadeias:
   print(f"S({x}) = {S(x)}")

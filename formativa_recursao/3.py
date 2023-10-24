def exponenciacao(base: int, expoente: int) -> int:
   if (expoente <= 0):
      return 1
   return base * exponenciacao(base, expoente - 1)

print(exponenciacao(3, 4))

def fatorial_iterativo(n: int) -> int:
   fatorial = 1
   for i in range(2, n + 1):
      fatorial *= i
   return fatorial

def fatorial_recursivo(n: int) -> int:
   if (n <= 1):
      return 1
   return n * fatorial_recursivo(n - 1)

print(fatorial_iterativo(5))
print(fatorial_recursivo(5))

def fibonacci_iterativo(termo: int) -> int:
   penultimo = 1
   ultimo = 1
   for _ in range(3, termo + 1):
      aux = penultimo
      penultimo = ultimo
      ultimo += aux
   return ultimo

def fibonacci_recursivo(termo: int) -> int:
   if (termo < 3):
      return 1
   return fibonacci_recursivo(termo - 1) + fibonacci_recursivo(termo - 2)

print(fibonacci_iterativo(11))
print(fibonacci_recursivo(11))

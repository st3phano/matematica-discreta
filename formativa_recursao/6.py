def contar_movimentos_torre_hanoi(pino_inicial: str,
                                  pino_auxiliar: str,
                                  pino_final: str,
                                  discos: int) -> int:
   if (discos == 0):
      return 0
   movimentos = 1
   movimentos += contar_movimentos_torre_hanoi(pino_inicial, pino_final, pino_auxiliar, discos - 1)
   print(f"move de {pino_inicial} para {pino_final}")
   movimentos += contar_movimentos_torre_hanoi(pino_auxiliar, pino_inicial, pino_final, discos - 1)

   return movimentos

print(contar_movimentos_torre_hanoi("inical", "auxiliar", "final", 4))

def ler_conjunto(arquivo, separador_elementos):
   conjunto = arquivo.readline()

   return set(x.strip() for x in conjunto.split(separador_elementos))

def ler_operacao(arquivo):
   return arquivo.readline().strip().upper()

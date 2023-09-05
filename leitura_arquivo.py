# Stéphano Roccato Trevisan

def ler_conjunto(arquivo):
   conjunto = arquivo.readline()

   SEPARADOR_ELEMENTOS = ','
   return set(x.strip() for x in conjunto.split(SEPARADOR_ELEMENTOS))

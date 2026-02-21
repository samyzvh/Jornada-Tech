# Tabuada automática

N1 = int(input("Tabuada de qualquer número: "))

for z in range(1,11): # "in range" é para executar o "para cada" no intervalo de inicio e fim
  # Total de voltas do for: (Fim - Inicio)
  print( N1, "x" , z ,"=", N1 * z ) # Também poderia printar assim: (f"{N1} x {c} = {N1 * c}")
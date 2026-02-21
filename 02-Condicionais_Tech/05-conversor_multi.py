# Conversor de moedas com opções

RL = float(input("Digite o valor em real: "))
DL = RL / 5.22
EU = RL / 6.19
tipo = str(input("Você quer converter o valor em dólar ou euro? "))

if tipo == "euro":
  print(f"R${RL:.2f} reais é exatamente U${EU:.2f} euros.")
else:
  print(f"R${RL:.2f} reais é exatamente U${DL:.2f} dólares.")
# Jogo de Adivinhação: Uso do random (tente adivinhar um número de 1 a 100)

import random # Ele tem o poder de sortear qualquer número que você determina: "entre x e y" (x,y)

nm = random.randint(1,100)
print("Adivinhe o número sorteado")
acertou = False

for tentativa in range(1, 6):
  print(f"Tentativa {tentativa} de 5")
  chute = int(input("Digite um número: "))

  if chute == nm:
    print("Parabéns!! Você acertou o número sorteado")
    acertou = True
    break
  elif chute < nm:
    print("O número é maior")
  else:
    print("O número é menor")

if not acertou:
  print(f"Suas chances acabaram. O numero era: {nm}")
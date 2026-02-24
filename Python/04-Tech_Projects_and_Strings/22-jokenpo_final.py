# Joguinho do JOKENPÔ

import random

jokenpo = ["Pedra", "Papel", "Tesoura"]

while True: # Enquanto tudo isso for verdade faça (só para no break)
    PC = random.choice(jokenpo) # random.choice é para ser usado em listas, para escolher um item aleatório da lista
    P1 = input("Jogue: ").capitalize() # Mesmo que ele digite a 1 letra minúscula o computador sempre vai trasnformar a 1 letra em maiúscula

    if P1 not in jokenpo: # Se o que o P1 digitar não estiver na lista do jokenpo faça:
        print("Opção inválida! Tente novamente.")
        continue # Se estiver, continue

    print(f"Computador escolheu: {PC}")

    escolha = input("Quer continuar s/n? ")
    if escolha.lower() != "s": # Para sempre ser minúsculo
        break